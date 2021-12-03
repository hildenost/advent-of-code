""" Advent of Code 2021. Day 3: Binary Diagnostic """

import numpy as np

with open("input.txt") as f:
    diagnostic = np.array([[int(l) for l in line] for line in f.read().splitlines()])


def from_binary(arr):
    return int("".join(str(int(a)) for a in arr), 2)


gamma_mask = diagnostic.sum(axis=0) > diagnostic.shape[0] / 2

gamma = from_binary(gamma_mask)
epsilon = from_binary(~gamma_mask)

print("Part 1:\t", gamma * epsilon)

# part 2
from operator import eq, ne


def find_rating(arr, op=eq):
    i = 0
    while len(arr) > 1:
        # filter arr based on column i equaling or not equaling
        # the sum of column i >= half of the length (to find the max occurence)
        arr = arr[op(arr[:, i], arr[:, i].sum() >= len(arr) / 2)]
        i += 1
    return from_binary(arr[0])


oxygen_rating = find_rating(diagnostic, op=eq)
co2_rating = find_rating(diagnostic, op=ne)
print("Part 2:\t", co2_rating * oxygen_rating)

