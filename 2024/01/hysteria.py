""" Advent of Code 2024. Day 1: Historian Hysteria """

with open("input.txt") as f:
    first, second = list(
        zip(*[[int(n) for n in l.split()] for l in f.read().splitlines()])
    )
part1 = sum(abs(a - b) for a, b, in zip(sorted(first), sorted(second)))
print("Part 1:\t", part1)


print("Part 2:\t", sum(n * second.count(n) for n in first))
