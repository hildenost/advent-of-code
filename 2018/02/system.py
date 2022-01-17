""" Advent of Code 2018. Day 2: Inventory Management System """
from collections import Counter
from math import comb

with open("input.txt") as f:
    boxes = f.read().splitlines()


counts = [
    {c[1] for c in Counter(boxid).most_common() if c[1] == 2 or c[1] == 3}
    for boxid in boxes
]

twos = sum(2 in t for t in counts)
threes = sum(3 in t for t in counts)
print("Part 1:\t", twos * threes)

import numpy as np

letter_matrix = np.array([list(boxid) for boxid in boxes])
# Compare all rows to eachother
cmp = letter_matrix[:, np.newaxis] != letter_matrix
# Get boxid-indices of 1-off ids
# Need only the first pair because they are the same
idc = np.where(cmp.sum(axis=2) == 1)[0]

print("Part 2:\t", "".join(a for a, b in letter_matrix[idc].T if a == b))
