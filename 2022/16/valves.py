""" Advent of Code 2022. Day 16: Proboscidea Volcanium """

with open("input.txt") as f:
    sample = f.read() 

import re

flowrates = [int(n) for n in re.findall(r"\d+", sample)]

# Creating adjacencies etc
valves = {}
rates = {}
for rate, line in zip(flowrates, sample.splitlines()):
    valve, *neighbours = re.findall(r"[A-Z]{2}", line)
    valves[valve] = neighbours
    rates[valve] = rate

# These are the only ones worth opening
vertices = {v for v in valves if rates[v] > 0}

from heapq import heappush
from heapq import heappop

def find_pressure(unopened):
    return sum(rates[v] for v in vertices if v not in unopened) 

def open_valves(valves, unopened):
    return tuple(v for v in unopened if v not in valves)

### Part 1
init_state = (0, "AA", tuple(sorted(vertices)))
new_states = {init_state}
visited = {init_state}

for t in range(30):
    states = new_states if t < 6 else sorted(new_states, key=lambda x: -x[0])[:2500]

    new_states = set()

    for pressure, current, to_open in states:
        new_pressure = pressure + find_pressure(to_open)

        # If opening current valve
        if current in to_open:
            new_open = open_valves([current], to_open)
            new_states.add((new_pressure, current, new_open))

        # If moving to new valve
        new_states.update({
            (new_pressure, neighbour, to_open) 
            for neighbour in valves[current]
        })

        visited.update(new_states)

print("Part 1:\t", max(new_states)[0])


### Part 2
init_state = (0, "AA", "AA", tuple(sorted(vertices)))
new_states = {init_state}
visited = {init_state}

for t in range(26):
    states = new_states if t < 6 else sorted(new_states, key=lambda x: -x[0])[:2500]

    new_states = set()

    for pressure, current, elephant, to_open in states:
        new_pressure = pressure + find_pressure(to_open)

        # If opening current valve
        if current in to_open and elephant not in to_open:
            new_open = open_valves([current], to_open)
            # Moving the elephant elsewhere
            new_states.update(
                (new_pressure, current, elephour, new_open) 
                for elephour in valves[elephant]
            )
        if elephant in to_open and current not in to_open:
            new_open = open_valves([elephant], to_open)
            # Moving myself elsewhere
            new_states.update(
                (new_pressure, neighbour, elephant, new_open) 
                for neighbour in valves[current]
            )
        if elephant in to_open and current in to_open:
            if elephant != current:
                new_open = open_valves([current, elephant], to_open)
                new_states.add((new_pressure, current, elephant, new_open))
            else:
                new_open = open_valves([elephant], to_open)
                # Moving myself elsewhere
                new_states.update(
                    (new_pressure, neighbour, elephant, new_open) 
                    for neighbour in valves[current]
                )

        # If moving to new valve
        new_states.update({
            (new_pressure, neighbour, elephour, to_open) 
            for neighbour in valves[current]
            for elephour in valves[elephant]
        })

        visited.update(new_states)

print("Part 2:\t", max(new_states)[0])
