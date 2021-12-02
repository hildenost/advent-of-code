""" Advent of Code 2020 Day 10: Adapter Array """

with open("10/input.txt") as f:
    adapters = sorted([int(l) for l in f.read().splitlines()])

### PART 1 regular python
curr = 0
diff = [0, 0, 0, 0]

for adapter in adapters:
    if 1 <= adapter - curr <= 3:
        diff[adapter - curr] += 1
        curr = adapter

# The 1 added to diff[3] is the final adapter
print(diff[1] * (diff[3] + 1))

### PART 1 numpy
import numpy as np

# Adding the initial outlet and final adapter
adapters = [0] + adapters + [max(adapters) + 3]
diffs = np.diff(adapters)
print((diffs == 1).sum() * (diffs == 3).sum())

### PART 2
# Dynamic programming and recursion!

# Initalising the path count dict
# Solution will be stored at counts[0]
counts = {k: 0 for k in adapters}
counts[adapters[-1]] = 1

# Adjacency matrix
# Created knowing that the children can be at most 3 indices away from
# current node
children = {
    k: [c for c in adapters[i + 1 : i + 4] if 1 <= c - k <= 3]
    for i, k in enumerate(adapters)
}


def dfs(start, end):
    if start == end:
        return 1

    if not counts[start]:
        counts[start] = sum(dfs(c, start) for c in children[start])
    return counts[start]


dfs(0, adapters[-1])
print(counts[0])
