""" Advent of Code 2018. Day 10: The Stars Align """
import re

import numpy as np

with open("input.txt") as f:
    points = np.array([
        tuple(int(n) for n in re.findall(r"-?\d+", line))
        for line in f.read().splitlines()])


def draw(points):
    xmax, ymax, *__ = points.max(axis=0)
    xmin, ymin, *__ = points.min(axis=0)

    if ymax - ymin > 10:
        return False


    print("Part 1:")
    ps = {(x, y) for x, y in points}
    for y in range(ymin, ymax+1):
        row = ""
        for x in range(xmin, xmax+1):
            row += "#" if (x, y) in ps else " "
        print(row)
    return True
    
vels = points[:, 2:]
points = points[:, :2]

from itertools import count
for s in count(1):
    points += vels
    if draw(points):
        break

print("Part 2:\t", s)
