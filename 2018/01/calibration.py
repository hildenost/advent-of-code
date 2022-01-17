""" Advent of Code 2018. Day 1: Chronal Calibration """

with open("input.txt") as f:
    frequencies = [int(n) for n in f.read().splitlines()]

print("Part 1:\t", sum(frequencies))


from itertools import cycle

current_frequency = 0
seen = {current_frequency}
for f in cycle(frequencies):
    current_frequency += f

    if current_frequency in seen:
        break

    seen.add(current_frequency)

print("Part 2:\t", current_frequency)

