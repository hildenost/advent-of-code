""" Advent of Code 2022. Day 19: Not Enough Minerals """

with open("input.txt") as f:
    sample = f.read().splitlines()

import re
def ints(text):
    return [[int(n) for n in re.findall(r"-?\d+", line)] for line in text]

def expand(costs, stash):
    geode, obs, clay, ore = stash 

    children = []
    if obs >= costs[5] and ore >= costs[4]:
        children.append(((geode, (obs-costs[5]), clay, (ore-costs[4])), (1, 0, 0, 0)))
    if clay >= costs[3] and ore >= costs[2]:
        children.append(((geode, obs, (clay-costs[3]), (ore-costs[2])), (0, 1, 0, 0)))
    if ore >= costs[1]:
        children.append(((geode, obs, clay, (ore-costs[1])), (0, 0, 1, 0)))
    if ore >= costs[0]:
        children.append(((geode, obs, clay, (ore-costs[0])), (0, 0, 0, 1)))

    children.append((stash, (0, 0, 0, 0)))
    return children

def update_stash(stash, bots):
    return tuple(a+b for a, b in zip(stash, bots))

def update_bots(bots, extra):
    return tuple(a+b for a, b in zip(bots, extra))


def bfs(costs, mins=24):
    # Initial states
    bots = (0, 0, 0, 1)
    stash = (0, 0, 0, 0)
    visited = {(bots, stash)}
    new_states = {(bots, stash)}

    for t in range(mins):
        states = new_states if t < 20 else sorted(new_states, reverse=True)[:100000]
        new_states = set()
        for bots, stash in states:
            for new_stash, new_bots in expand(costs, stash):
                new_bots = update_bots(bots, new_bots)
                new_stash = update_stash(new_stash, bots)
                if (new_bots, new_stash) not in visited:
                    new_states.add((new_bots, new_stash))

        visited.update(new_states)
    return max(n for *__, (n, *__) in new_states)

total = 0
for blueprint, *costs in ints(sample):
    geodes = bfs(costs, mins=24)
    total += blueprint * geodes 
print("Part 1:\t", total)

total = 1
for blueprint, *costs in ints(sample)[:3]:
    geodes = bfs(costs, mins=32)
    total *= geodes 
print("Part 2:\t", total)
