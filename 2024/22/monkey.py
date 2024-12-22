""" Advent of Code 2024. Day 22: Monkey Market """

import numpy as np


def generate_next(number):
    temp = number * 64
    number ^= temp
    number %= 16777216

    temp = number // 32
    number ^= temp
    number %= 16777216

    temp = number * 2048
    number ^= temp
    number %= 16777216

    return number


def prices(n):
    return n % 10


with open("input.txt") as f:
    n = np.array([int(n) for n in f.read().splitlines()])

p = [prices(n)]

from collections import defaultdict

bananas = defaultdict(int)
sold = defaultdict(set)

for __ in range(2000):
    n = generate_next(n)
    p.append(prices(n))
    p = p[-5:]
    if len(p) < 5:
        # No diff sequence before we have a history of 5 prices
        continue

    diffs = np.diff(np.array(p), axis=0)[-4:]

    for i, (d, price) in enumerate(zip(diffs.T.tolist(), p[-1])):
        if i in sold[(tuple(d))]:
            # Don't sell again to this monkey
            continue
        bananas[tuple(d)] += price
        sold[(tuple(d))].add(i)

print("Part 1:\t", n.sum())
print("Part 2:\t", max(bananas.values()))
