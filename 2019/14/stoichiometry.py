""" 2019 Day 14: Space Stoichimetry """

with open("input.txt") as f:
    reactions = f.read()

from collections import defaultdict

START = "FUEL"
END = "ORE" 

digraph = defaultdict(set)
recipes = {}
for line in reactions.splitlines():
    left, right = line.split(" => ")

    v, k = right.split()
    output = (k, int(v))

    inputs = []
    for l in left.split(","):
        v, n = l.split()
        inputs.append((n, int(v)))
        digraph[k].add(n)

    recipes[output] = inputs


import math

def compute_ore(topological, n_fuel=1):
    totals = defaultdict(int)
    totals[START] = n_fuel

    for next_el in topological:

        # This hack here finds the correct amount needed
        # for that particular ingredient
        i = 1
        while not recipes.get((next_el, i), False):
            i += 1

        # The round-up factor needed
        n = math.ceil(totals[next_el] / i)

        for j, k in recipes[(next_el, i)]:
            totals[j] += n*k

    return totals[END]

def topological_sort(digraph):
    indegrees = {node: 0 for node in digraph} 
    for node in digraph:
        for neighbour in digraph[node]:
            if neighbour != END:
                indegrees[neighbour] += 1


    outer_nodes = [node for node in digraph if indegrees[node] == 0]

    topological_order = []

    while outer_nodes:
        node = outer_nodes.pop()

        topological_order.append(node)

        for neighbour in digraph[node]:
            if neighbour == END:
                continue
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                outer_nodes.append(neighbour)

    return topological_order


topological = topological_sort(digraph)
ore = compute_ore(topological)
print("Part 1:\t", ore)

## PART 2
# Do binary search
TRILLION = 1_000_000_000_000
fuel_lower = TRILLION / ore
fuel_upper = TRILLION
while fuel_lower != fuel_upper:
    fuel_mid = (fuel_lower + fuel_upper) // 2
    ore_mid = compute_ore(topological, fuel_mid)

    if TRILLION > ore_mid:
        fuel_lower = fuel_mid + 1
        final_fuel = fuel_upper

    elif TRILLION < ore_mid:
        fuel_upper = fuel_mid - 1
        final_fuel = fuel_lower
print("Part 2:\t", int(final_fuel))
