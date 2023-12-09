""" Advent of Code 2023. Day 9: Mirage Maintenance """

with open("input.txt") as f:
    report = [[int(n) for n in line.split()] for line in f.readlines()]

# Naive


def diff(numbers):
    return [b - a for a, b in zip(numbers, numbers[1:])]


added = 0
for history in report:
    while any(history):
        added += history[-1]
        history = diff(history)
print("Part 1:\t", added)

subbed = 0
for history in report:
    hs = []
    while any(history):
        hs.append(history[0])
        history = diff(history)

    temp = 0
    for h in hs[::-1]:
        temp = h - temp

    subbed += temp
print("Part 2:\t", subbed)
