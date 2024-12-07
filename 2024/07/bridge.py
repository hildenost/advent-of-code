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


def calibrate(valid_ops="*+"):
    total_sum = 0
    for value, first, *numbers in equations:
        for combos in product(valid_ops, repeat=len(numbers)):
            total = first
            for n, op in zip(numbers, combos):
                total = ops[op](total, n)
                # Down the wrong path, abort
                if total > value:
                    continue
            if total == value:
                total_sum += value
                break
    return total_sum


print("Part 1:\t", calibrate("*+"))
print("Part 2:\t", calibrate("*+|"))
