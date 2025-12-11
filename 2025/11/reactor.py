"""Advent of Code 2025. Day 11: Reactor"""

with open("input.txt") as f:
    lines = f.read().splitlines()

example = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".splitlines()
# lines = example

graph = {}
for line in lines:
    node, children = line.split(":")
    children = children.split()
    graph[node] = children


start = "you"
stack = [start]
paths = 0
while stack:
    node = stack.pop()

    if node == "out":
        paths += 1
        continue

    stack.extend(graph[node])

print("Part 1:\t", paths)

from collections import defaultdict

# Create edges
edges = set()
for node in graph:
    for child in graph[node]:
        edges.add(frozenset((node, child)))

# Going backwards
parents = defaultdict(set)
for node in graph:
    for child in graph[node]:
        parents[child].add(node)

# Do topological sorting
start = "svr"
S = {start}
L = []

while S:
    n = S.pop()
    if n == "out":
        continue
    L.append(n)
    for child in graph[n]:
        edges.remove({child, n})
        if not any({parent, child} in edges for parent in parents[child] - {n}):
            S.add(child)
assert len(L) == len(graph)
L.append("out")

n_parents = {child: len(p) for child, p in parents.items()}


def count(start, end):
    test_paths = defaultdict(int)

    __, i = start
    endnode, __ = end

    test_paths[L[i]] = 1
    for node in L[i + 1 :]:
        test_paths[node] = sum(test_paths[p] for p in parents[node])
        if node == endnode:
            return test_paths[node]


# Find whether fft comes before dac in the topological sort
# or the other way round
fft_i = L.index("fft")
dac_i = L.index("dac")
nodes = {"svr": 0, "dac": dac_i, "fft": fft_i, "out": len(L) - 1}
sorted_nodes = sorted(nodes.items(), key=lambda n: n[1])
import math

paths = math.prod(count(a, b) for a, b in zip(sorted_nodes, sorted_nodes[1:]))
print("Part 2:\t", paths)
