""" Advent of Code 2018. Day 24: Immune System Simulator 20XX """

armies = """Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
"""
import re

pattern = re.compile(r"(\d+) units each with (\d+) hit points.*?with an attack that does (\d+) (\w+) damage at initiative (\d+)")
weaknesses = re.compile(r"(\w+) to (\w+),? ?(\w+)?,? ?(\w+)?,? ?(\w+)?")

with open("input.txt") as f:
    armies = f.read()

immune_army, infection_army = armies.strip().split("\n\n")

class Group:
    def __init__(self, units, hp, strength, side, weak=None, immune=None, damagetype=None, initiative=0, id=0):
        self.units = units
        self.hp = hp
        self.strength = strength
        
        self.weak = weak if weak is not None else []
        self.immune = immune if immune is not None else []
        self.damagetype=damagetype

        self.initiative = initiative

        self.type = side

        self.id = id


    def effective_power(self):
        return self.units * self.strength

    def __lt__(self, other):
        return (self.effective_power(), self.initiative) < (other.effective_power(), other.initiative)

    def __repr__(self):
        return f"Group({self.type}, {self.id}, units={self.units}, hp={self.hp})"

    def __eq__(self, other):
        return (self.hp, self.strength, tuple(self.weak), tuple(self.immune), self.damagetype, self.initiative, self.type) == (other.hp, other.strength, tuple(other.weak), tuple(other.immune), other.damagetype, other.initiative, other.type)

    def __hash__(self):
        return hash((self.hp, self.strength, tuple(self.weak), tuple(self.immune), self.damagetype, self.initiative, self.type))

def create_army(army, side):
    complete = []
    for i, line in enumerate(army.splitlines()[1:]):
        m = re.search(pattern, line)
        units, hp, strength, damagetype, initiative = m.groups()
        group = Group(int(units), int(hp), int(strength), damagetype=damagetype, initiative=int(initiative), side=side, id=i+1)

        for w in re.findall(weaknesses, line):
            if w[0] == "immune":
                group.immune = [t for t in w[1:] if t]
            else:
                group.weak = [t for t in w[1:] if t]

        complete.append(group)
    return complete


def print_status(infection, immunesystem):
    print("Immune System:")
    if not immunesystem:
        print("No groups remain.")
    for group in immunesystem:
        print(group)
    print("Infection:")
    if not infection:
        print("No groups remain.")
    for group in infection:
        print(group)
    print()

def fight(immune_army, infection_army, boost=0):
    immunesystem = create_army(immune_army, side="Immune System")
    infection = create_army(infection_army, side="Infection")

    for group in immunesystem:
        group.strength += boost

    # A round
    i = 0
    while True:
        # Filtering out the dead ones
        immunesystem = [i for i in immunesystem if i.units > 0]
        infection = [i for i in infection if i.units > 0]

        if not immunesystem:
            return False, sum(i.units for i in infection)
        if not infection:
            return True, sum(i.units for i in immunesystem)

        if i > 20000:
            # Stalemate
            return False, 0

        # 1. Target selection
        targets = {}
        for group in sorted(immunesystem + infection, reverse=True):
            if group.type == "Immune System":
                enemies = [i for i in infection if i not in targets]
            else:
                enemies = [i for i in immunesystem if i not in targets]

            damage = group.effective_power()
            deals = {}
            for e in enemies:
                #print("Weaknesses: ", e.weak)
                #print("Immunity:   ", e.immune)
                if group.damagetype in e.immune:
                    #print("They immune")
                    deals[e] = (0, e.effective_power(), e.initiative)
                elif group.damagetype in e.weak:
                    #print("They weak, deal double")
                    deals[e] = (2*damage, e.effective_power(), e.initiative)
                else:
                    deals[e] = (damage, e.effective_power(), e.initiative)

            if not deals:
                group.target = None
                continue

            #print(deals)
            target, (d, *__) = max(deals.items(), key=lambda x: x[1])
            if d == 0:
                group.target = None
                continue

            group.target = target
            #print(target)
            if group.type == "immune":
                targets[group.target] = d
            else:
                targets[group.target] = d

        # 2. Attack
        for group in sorted(immunesystem + infection, key=lambda x: x.initiative, reverse=True):
            if group.target is None:
                continue
            if group.units <= 0:
                continue

            damage = group.effective_power()
            if group.damagetype in group.target.immune:
                damage = 0
            elif group.damagetype in group.target.weak:
                damage *= 2

            loss = damage // group.target.hp

            group.target.units -= loss

        i += 1


immune_won_lower, units = fight(immune_army, infection_army)
print("Part 1:\t", units)

#### Part 2 ####

# Guessing the upper value roughly
lower = 0
upper = 100

immune_won, __ = fight(immune_army, infection_army, boost=upper)
while not immune_won:
    upper += 100
    immune_won, __ = fight(immune_army, infection_army, boost=upper)

immunity = (immune_won_lower, immune_won)
while lower != upper:
    mid = (lower + upper) // 2

    is_immune_mid, units = fight(immune_army, infection_army, boost=mid)

    if (mid == lower or mid == upper):
        __, units = fight(immune_army, infection_army, boost=upper)
        print("Part 2:\t", units)
        break

    if is_immune_mid:
        upper = mid
    else:
        lower = mid

