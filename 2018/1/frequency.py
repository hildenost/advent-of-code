"""Advent of code 2018: 1/2 on 1 Dec

Finding and printing current frequency.

"""

with open("input.txt") as f:
    print(sum(int(line) for line in f.readlines()))
