""" Advent of Code 2017. Day 21: Fractal Art """

import numpy as np

pattern = """.#.
..#
###
""".splitlines()

def to_array(p):
    return np.array([[c == "#" for c in line] for line in p])

def create_rules(A):
    return np.array([
        A,
        A[::-1],
        A[:,::-1],
        A[::-1,::-1],
        A.T,
        A.T[::-1],
        A.T[:,::-1],
        A.T[::-1,::-1]
        ]
    )

start = to_array(pattern)

with open("input.txt") as f:
    raw_rules = f.read().splitlines()

def to_binary(p):
    return "".join(str(int(c)) for c in p.reshape(-1))

from collections import defaultdict
rules = defaultdict(dict)
for rule in raw_rules:
    p, r = rule.split(" => ")
    p = p.split("/")

    r = to_array(r.split("/"))

    binaries = set([to_binary(n) for n in create_rules(to_array(p))])

    rules[len(p)].update({int(k, 2): r for k in binaries})


def get_next(p):
    return rules[p.shape[0]][int(to_binary(p), 2)]

from itertools import product
pattern = start
for i in range(18):
    divisor = 3 if pattern.shape[0] % 2 else 2

    new_shape = (divisor + 1) * pattern.shape[0] // divisor
    next_pattern = np.zeros((new_shape, new_shape), dtype=bool)

    old_slices = [slice(i, i+divisor, 1) for i in range(0, pattern.shape[0], divisor)]
    slices = [slice(i, i+divisor+1, 1) for i in range(0, new_shape, divisor+1)]

    for (a, b), (c, d) in zip(product(old_slices, repeat=2), product(slices, repeat=2)):
        next_pattern[(c, d)] = get_next(pattern[(a, b)])
    
    pattern = next_pattern
    
    if i == 4:
        print("Part 1:\t", pattern.sum())
print("part 2:\t", pattern.sum())

