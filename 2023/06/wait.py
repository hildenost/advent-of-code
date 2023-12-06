""" Advent of Code 2023. Day 6: Wait For It """
import math

with open("input.txt") as f:
    times, records = [[int(n) for n in l.split()[1:]] for l in f.readlines()]

ways = 1
for T, r in zip(times, records):
    count = 0
    for t in range(T + 1):
        distance = (T - t) * t
        count += distance > r
    ways *= count
print("Part 1:\t", ways)


def quadratic(a, b, c):
    q = math.sqrt(b * b - 4 * a * c)
    return int((-b + q) / (2 * a)), int((-b - q) / (2 * a))


times = int("".join(str(t) for t in times))
record = int("".join(str(r) for r in records))
upper, lower = quadratic(1, -times, record)
print("Part 2:\t", upper - lower)
