""" Advent of Code 2024. Day 25: Code Chronicle """

with open("input.txt") as f:
    items = f.read().split("\n\n")

from collections import defaultdict

keys = []
locks = []

for item in items:
    lines = item.strip().splitlines()

    # Check pin heights
    pins = [0, 0, 0, 0, 0]
    for line in lines[1:-1]:
        for i, p in enumerate(line):
            if p == "#":
                pins[i] += 1
    # Check top row = lock
    if lines[0] == "#" * 5:
        locks.append(pins)
    # Check bottom row = key
    elif lines[-1] == "#" * 5:
        keys.append(pins)

number_of_matches = sum(
    all((k + l) <= 5 for k, l in zip(key, lock)) for key in keys for lock in locks
)
print("Part 1:\t", fits, number_of_matches)
