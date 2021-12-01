""" Advent of Code 2021. Day 1: Sonar Sweep """
import numpy as np

with open("input.txt") as f:
    scanning = [int(line) for line in f.read().splitlines()]

# np.diff finds the difference between element i+1 and i
# array > 0 returns a Boolean array where each element in array is checked
# True equals 1, so I just sum the Boolean array to find the answer
part1 = sum(np.diff(scanning) > 0)
print("PART 1:\t", part1)
# BONUS
# Solution WITHOUT numpy
part1 = sum(b - a > 0 for a, b in zip(scanning, scanning[1:]))
print("PART 1:\t", part1, "\t(native python)")

# python only zips as long as all iterables have elements
rolling = [(a + b + c) for a, b, c in zip(scanning, scanning[1:], scanning[2:])]
# Same procedure as in Part 1
part2 = sum(np.diff(rolling) > 0)
print("PART 2:\t", part2)
# BONUS
# Solution WITHOUT numpy
part2 = sum(b - a > 0 for a, b in zip(rolling, rolling[1:]))
print("PART 2:\t", part2, "\t(native python)")

