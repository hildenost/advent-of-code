""" Advent of Code 2021. Day 8: Seven Segment Search """


import re

with open("input.txt") as f:
    displays = f.read().splitlines()

counter = sum(len(d) in [2, 3, 4, 7] for display in displays for d in display.split()[-4:])
print("Part 1:\t", counter)
