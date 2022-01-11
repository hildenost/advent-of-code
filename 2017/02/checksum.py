""" Advent of Code 2017. Day 2: Corruption Checksum """

with open("input.txt") as f:
    spreadsheet = [[int(n) for n in line.split("\t")] for line in f.read().splitlines()]

def checksum(sheet):
    return sum(max(row) - min(row) for row in sheet)

from itertools import permutations
def evenly(sheet):
    return sum(a // b
        for row in sheet
        for a, b in permutations(row, 2)
        if a % b == 0)

print("Part 1:\t", checksum(spreadsheet))
print("Part 2:\t", evenly(spreadsheet))
