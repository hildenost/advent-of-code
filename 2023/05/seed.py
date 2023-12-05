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


def find_value(value, n, dest, source, length):
    # Check if value and value + n falls within the source range
    # Truncate to source range
    left = max(value, source)
    right = min(value + n, source + length)

    if right < left:
        # Nope, this doesn't work
        return (0, 0)

    # Finding the appropriate new range
    return dest + (left - source), right - left


locs = set()
for seed in seeds:
    v = seed
    for mapping in instr:
        new_v = sum(find_value(v, 0, *line)[0] for line in mapping)
        v = new_v if new_v else v
    locs.add(v)
print("Part 1:\t", min(locs))
assert min(locs) == 462648396
import time

start = time.time()


locs = set()
for seed, span in zip(seeds[::2], seeds[1::2]):
    ranges = {(seed, span)}
    for mapping in instr:
        new_ranges = set()
        for v, n in ranges:
            subranges = {find_value(v, n, *line) for line in mapping} - {(0, 0)}

            n_mapped = sum(b for _, b in subranges)
            if n_mapped != n:
                # We still have not mapped all of original values
                # Add the remaining
                subranges.add((v, n - n_mapped))

            new_ranges.update(subranges)
        ranges = new_ranges

    location = min(a for a, _ in ranges)
    locs.add(location)
print("Part 2:\t", min(locs))
end = time.time()
print(end - start)
assert min(locs) == 2520479
