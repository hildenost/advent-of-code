""" Advent of Code 2018. Day 12: Subterranean Sustainability """

with open("input.txt") as f:
    initial, rules = f.read().split("\n\n")

state = initial.split()[-1]

rules = dict(line.split(" => ") for line in rules.splitlines())

def sum_pots(state, offset=0):
    return sum(i-offset for i, l in enumerate(state) if l == "#")

def simulate(state, n_gens=20):
    seen = set()
    for g in range(n_gens): 
        state = "..." + state + "..."
        state = "".join(rules[state[i-2:i+3]] for i in range(2, len(state)-2))

        # Check whether we've seen this equivalent state before
        stripped = state.strip(".")
        if stripped in seen:
            # Per generation, the first # shifts 2 place to the right
            return sum_pots(state, offset=2*(g+1) - n_gens)
        
        seen.add(stripped)

    return sum_pots(state, offset=n_gens) 

print("Part 1:\t", simulate(state))

fifty_billion = 50000000000
print("Part 2:\t", simulate(state, n_gens=fifty_billion))





