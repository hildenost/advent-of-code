""" Advent of Code 2023. Day 5: If You Give A Seed A Fertilizer """


import re

with open("test_input.txt") as f:
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
    print("==== SEED and RANGE ", seed, span)
    ranges = {(seed, span)}
    for mapping in instr:
        new_ranges = set()
        print()
        print()
        print()
        print(ranges)
        for v, n in ranges:
            leftovers = []
            subranges = set()
            for line in mapping:
                new_v, new_n, left, right = find_value(v, n, *line)
                print(new_v, new_n, left, right)
                if new_n == n:
                    subranges.add((new_v, new_n))
                elif new_n != n and new_n > 0:
                    leftovers.append((max(v, left), min(right, v + n)))
                    subranges.add((new_v, new_n))
                else:
                    subranges.add((new_v, new_n))
            print(leftovers)
            subranges.discard((0, 0))
            if subranges:
                new_span = sum(b for a, b in subranges)
                print("NEW SPAN: ", new_span)
                print("Input ranges: ", (v, n))
                print("Output ranges: ", subranges)
                new_ranges = new_ranges.union(subranges)
                print(new_ranges)
            else:
                print("NO NEW RANGES!!!!")
                print((v, n))
                new_ranges.add((v, n))
        ranges = new_ranges
    print(seed, span, ranges)
    print()

    locs.append(v)
    break
