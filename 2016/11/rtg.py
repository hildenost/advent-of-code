""" Advent of Code 2016. Day 11: Radioisotope Thermoelectric Generators """

floors = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
""".splitlines()

floors = """The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
""".splitlines()
import re

def parse(floors):
    pattern = re.compile(r"(\w+)(?:-\w+)? (microchip|generator)")
    return [re.findall(pattern, floor) for floor in floors]

floors = parse(floors)

"""
rules

elevator:
    must have rtg or microchip, but max 2 items
    items can irradiate eachother at stops, but ok if M and G connected
    a M cannot pass another G without its matching G

# Hva er egentlig en passende datastruktur???
"""
class Item:
    def __init__(self, fuel):
        self.fuel = fuel
    def __eq__(self, other):
        return self.fuel == other.fuel and type(self) == type(other)

    def __hash__(self):
        return hash(repr(self))

    def __lt__(self, other):
        return self.__repr__() < other.__repr__() 

class RTG(Item):
    def __repr__(self):
        return f"RTG({self.fuel})"


class Chip(Item):
    def __repr__(self):
        return f"Chip({self.fuel})"

def evaluate(state):
    generators = [c for c in state if isinstance(c, RTG)]
    # Special case if no generators on floor, it's ok
    if not generators:
        return True

    for m in state:
        if isinstance(m, Chip) and not RTG(m.fuel) in generators:
            return False
    return True

from itertools import combinations

def expand(node):
    current_floor = node.state[node.current]
    # Choose what items to select


    steps = []
    # First generate all combos
    # Either 1 item
    steps.extend([{i} for i in current_floor])
    # Or a combination of 2 items
    steps.extend([set(c) for c in combinations(current_floor, 2)])

    # Then filter the illegal ones 
    steps = [step
        for step in steps
        if evaluate(step) and
           evaluate(current_floor - set(step))
    ]

    # If there are several RTG/chip pairs, they are interchangeable
    # I can select just one couple and let the rest be, reducing the
    # solution space
    found_chip = False
    found_chips = False
    found_rtg = False
    found_rtgs = False
    found_pair = False
    final_steps = []
    for s in steps:
        if len(s) == 1:
            (i,) = s
            if isinstance(i, Chip) and not found_chip:
                final_steps.append(s)
                found_chip = True
            elif isinstance(i, RTG) and not found_rtg:
                final_steps.append(s)
                found_rtg = True
        else:
            if all(isinstance(i, Chip) for i in s):
                if not found_chips:
                    final_steps.append(s)
                    found_chips = True
            elif all(isinstance(i, RTG) for i in s):
                if not found_rtgs:
                    final_steps.append(s)
                    found_rtgs = True
            else:
                if not found_pair:
                    final_steps.append(s)
                    found_pair = True

    steps = final_steps

    # Need to check both directions: up and down
    queue = []
    for d in (1, -1):
        next_floor = node.current + d

        # If this floor doesn't exist, just skip
        if not 0 <= next_floor <= 3:
            continue

        for s in steps:
            if d == -1 and len(s) == 2:
                # We don't bother carrying things downwards
                continue
            if evaluate(set(s).union(node.state[next_floor])):
                # This means that we can move the selected items
                # to the next floor
                queue.append(Node(move(node, s, d), next_floor, node.g + 1)) 
    return queue

class Node:
    def __init__(self, state, current=0, cost=0):
        self.state = state
        self.current = current 
        self.g = cost
        self.h = self.heuristic()
        self.score = self.g + self.h

    def __eq__(self, other):
        return self.state == other.state and self.current == other.current

    def __hash__(self):
        return hash(tuple(tuple(sorted(floor)) for floor in self.state))

    def __lt__(self, other):
        if self.score == other.score:
            return self.g < other.g
        return self.score < other.score

    def heuristic(self):
        return sum((3-i)*len(floor) for i, floor in enumerate(self.state))


def move(node, items, direction):
    new_state = [{i for i in n} for n in node.state]
    for item in items:
        new_state[node.current].remove(item)
        new_state[node.current + direction].add(item)
    return new_state

from heapq import heappush
from heapq import heappop

def astar(startnode):
    open_list = [startnode] 
    closed_list = set()

    while open_list:
        n = heappop(open_list) 

        if n in closed_list:
            continue

        closed_list.add(n)

        if n.h == 0:
            print("Explored ", len(closed_list), " nodes")
            return n.g
       
        children = expand(n)

        for c in children:
            if c in closed_list:
                continue
            heappush(open_list, c)
    print("Explored ", len(closed_list), " nodes")

floors = [set([Chip(fuel) if typ == "microchip" else RTG(fuel)
          for fuel, typ in floor])
          for floor in floors]

part1 = astar(Node(floors))
print("Part 1:\t", part1) 

floors[0].update({RTG("elerium"), Chip("elerium"), RTG("dilithium"), Chip("dilithium")})
print("Part 2:\t", astar(Node(floors)))
