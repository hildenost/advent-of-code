""" Advent of Code 2024. Day 7: Bridge Repair """
import re

with open("input.txt") as f:
    equations = [[int(n) for n in re.findall("\d+", l)] for l in f.read().splitlines()]

ops = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "|": lambda a, b: int(str(a) + str(b)),
}

from itertools import product

total_sum = 0
for value, first, *numbers in equations:
    for combos in product("*+", repeat=len(numbers)):
        total = first
        for n, op in zip(numbers, combos):
            total = ops[op](total, n)
            if total > value:
                continue
        if total == value:
            total_sum += value
            break
print("Part 1:\t", total_sum)

total_sum = 0
for value, first, *numbers in equations:
    for combos in product("*+|", repeat=len(numbers)):
        total = first
        for n, op in zip(numbers, combos):
            total = ops[op](total, n)
            if total > value:
                continue
        if total == value:
            total_sum += value
            break
print("Part 2:\t", total_sum)
