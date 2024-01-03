""" Advent of Code 2023. Day 25: Snowverload """

with open("input.txt") as f:
    diagram = f.read().splitlines()

from collections import defaultdict

graph = defaultdict(list)

for line in diagram:
    name, *comps = line.split()
    name = name.strip(":")

    graph[name].extend(comps)
    for comp in comps:
        graph[comp].append(name)

# My not so robust algo, but it worked

cut = defaultdict(lambda: 0)
cut[name] = 1

A = set()
while sum(cut.values()) != 3 and graph:
    # Select next node
    node = max(cut, key=cut.get)
    # And remove it from the selection
    del cut[node]

    # Add node to partition A
    A.add(node)
    # Add the edges of the node to the cut
    for neighbour in graph[node]:
        if neighbour not in A:
            cut[neighbour] += 1

    # Remove node from graph
    del graph[node]

print("Part 1:\t", len(A) * len(graph))
