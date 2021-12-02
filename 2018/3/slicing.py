""" Day 3: No Matter How You Slice It """
import re
import sys

from itertools import combinations
import numpy as np

class Claim:
    def __init__(self, **match):
        self.__dict__.update(**match)
        self.overlap = False

    def __repr__(self):
        return str(self.__dict__)

def overlaps(minA, maxA, minB, maxB):
    return minB < maxA and minA < maxB

def is_overlapping(claimA, claimB):
    return (overlaps(claimA.x_min, claimA.x_min + claimA.width,
                     claimB.x_min, claimB.x_min + claimB.width)
           and
           overlaps(claimA.y_min, claimA.y_min + claimA.height,
                    claimB.y_min, claimB.y_min + claimB.height))

def parse_claim(claim):
    """ Parse input on the shape of

    #1 @ 1,3: 4x4

    which means ID 1 and rectangle upper left corner at 1,3
    with width x height 4x4.

    """
    pattern = (r"#(?P<id>\d+)"
               r" @ (?P<x_min>\d+),(?P<y_min>\d+):"
               r" (?P<width>\d+)x(?P<height>\d+)")
    match = re.search(pattern, claim)
    results = {k: int(v) for k, v in match.groupdict().items()}
    return Claim(**results)

claims = [parse_claim(line) for line in sys.stdin.readlines()]

# Brute force with hash map
pairs = combinations(claims, 2)
fabric = np.zeros((1000,1000), int)

for claimA, claimB in pairs:
    if is_overlapping(claimA, claimB):
        # Marking claims for Part 2
        claimA.overlap = True
        claimB.overlap = True

        x_min = max(claimA.x_min, claimB.x_min)
        x_max = min(claimA.x_min+claimA.width, claimB.x_min+claimB.width)
        y_min = max(claimA.y_min, claimB.y_min)
        y_max = min(claimA.y_min+claimA.height, claimB.y_min+claimB.height)
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                fabric[x,y] = 1

# Part 1 solution
print(np.sum(fabric))

# Part 2 solution
print([claim.id for claim in claims if not claim.overlap])
