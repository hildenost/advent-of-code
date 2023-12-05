""" Advent of Code 2023. Day 5: If You Give A Seed A Fertilizer """


import re

with open("input.txt") as f:
    (
        seeds,
        *instr,
    ) = f.read().split("\n\n")


seeds = [int(seed) for seed in seeds.split()[1:]]


def parse_almanac(chunk):
    return [[int(n) for n in line.split()] for line in chunk.splitlines()[1:]]


instr = [parse_almanac(mapping) for mapping in instr]

instr = [sorted(mapping, key=lambda x: x[1]) for mapping in instr]


def find_value(value, dest, source, length):
    # print(source, value, source + length)
    if value < source:
        # Too small seed number to fit
        return False

    if value >= source + length:
        # Too large seed number to fit
        return False

    diff = value - source
    return dest + diff


locs = []
for seed in seeds:
    v = seed
    for mapping in instr:
        new_v = sum(find_value(v, *line) for line in mapping)
        v = new_v if new_v else v
    locs.append(v)
print("Part 1:\t", min(locs))

import time

start = time.time()


def find_value(value, n, dest, source, length):
    # Check if value and value + n falls within the source range
    # Truncate to source range
    left = max(value, source)
    right = min(value + n, source + length)

    if right <= left:
        # Nope, this doesn't work
        return (0, 0, 0, 0)

    # Finding the appropriate new range
    diff_v = left - source
    n = right - left

    return dest + diff_v, n, left, right


locs = []
for seed, span in zip(seeds[::2], seeds[1::2]):
    ranges = {(seed, span)}
    for mapping in instr:
        new_ranges = set()
        for v, n in ranges:
            leftovers = []
            subranges = set()
            for line in mapping:
                new_v, new_n, left, right = find_value(v, n, *line)
                if new_n == n:
                    subranges.add((new_v, new_n))
                elif new_n != n and new_n > 0:
                    if right == v + n:
                        leftovers.append((v, left - v))
                    elif left == v:
                        leftovers.append((right, v + n - right))
                    else:
                        leftovers.append((right, v + n - right))
                        leftovers.append((v, left - v))

                    subranges.add((new_v, new_n))
                else:
                    subranges.add((new_v, new_n))
            subranges.discard((0, 0))
            if subranges:
                new_span = sum(b for a, b in subranges)
                if new_span != n:
                    subranges = subranges.union(set(leftovers))
                new_ranges = new_ranges.union(subranges)
            else:
                new_ranges.add((v, n))
        ranges = new_ranges
    v = min(a for a, b in ranges)
    locs.append(v)
print(min(locs))
end = time.time()
print(end - start)
