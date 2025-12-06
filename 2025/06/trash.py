""" Advent of Code 2025. Day 6: Trash Compactor"""
from math import prod

with open("input.txt") as f:
    *numbers, ops = f.read().splitlines()

def to_numbers(numbers):
    return [[int(n) for n in row.split()] for row in numbers]

def transpose(numbers):
    """Transpose the input and split into groups"""
    return to_numbers("\n".join(
        "" if not any(ns) else "".join(ns).strip()
        # must strip to be able to split correctly later
        for ns in zip(*numbers)
        ).split("\n\n"))

funcs = [sum if op == "+" else prod for op in ops.split()] 
    
rowsum = sum(
    func(t)
    for *t, func in zip(*to_numbers(numbers), funcs)
)
print("Part 1:\t", rowsum)


rowsum = sum(
    func(t)
    for t, func in zip(transpose(numbers), funcs)
)
print("Part 2:\t", rowsum)

