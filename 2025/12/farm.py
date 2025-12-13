"""Advent of Code 2025. Day 12: Christmas Tree Farm"""

import numpy as np
import re

with open("input.txt") as f:
    *presents, trees = f.read().split("\n\n")

# Parsing presents into a numpy boolean array
presents = [
    np.array([[col == "#" for col in row] for row in p.splitlines()[1:]])
    for p in presents
]
present_areas = [p.sum() for p in presents]
trees = [[int(n) for n in re.findall(r"\d+", tree)] for tree in trees.splitlines()]


def count_tiles(npresents, areas):
    return sum(n * a for n, a in zip(npresents, areas))


# Let's do a first sort, just counting tiles needed and comparing to tiles
# available without regarding orientation or anything
trees = [
    tree for tree in trees if tree[0] * tree[1] >= count_tiles(tree[2:], present_areas)
]
# And this initial sort was enough for a gold star
print("Part 1:\t", len(trees))
