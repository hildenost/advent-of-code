""" Advent of Code 2021. Day 7: The Treachery of Whales """

from numpy import abs

pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

with open("input.txt") as f:
    pos = [int(n) for n in f.read().split(",")]

part1 = min([sum(abs(p - i) for p in pos) for i in range(max(pos) + 1)])

part2 = min(
    # triangle numbers for computing the cost of fuel
    [sum(abs(p - i) * (abs(p - i) + 1) // 2 for p in pos) for i in range(max(pos) + 1)]
)

print("Part 1:\t", part1)
print("Part 2:\t", part2)

