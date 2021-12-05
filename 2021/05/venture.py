""" Advent of Code 2021. Day 5: Hydrothermal Venture """

import re
from itertools import zip_longest
from collections import Counter

with open("input.txt") as f:
    vents = f.read()

pattern = r"(\d+),(\d+) -> (\d+),(\d+)"
coords = [[int(l) for l in line] for line in re.findall(pattern, vents)]

def get_range(start, end):
    step = 1 if end > start else -1
    return range(start, end+step, step)

def find_crosses(coords, noangle=False):
    return sum(
        c > 1 for c in Counter(
            (x, y)
            for x1, y1, x2, y2 in coords
            for x, y in zip_longest(
                get_range(x1, x2),
                get_range(y1, y2),
                fillvalue=x1 if x1 == x2 else y1
            ) 
            if (noangle and (x1 == x2 or y1 == y2)) or not noangle
        ).values()) 


print("Part 1:\t", find_crosses(coords, noangle=True))
print("Part 2:\t", find_crosses(coords))
