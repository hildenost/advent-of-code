""" Advent of Code 2022. Day 15: Beacon Exclusion Zone """

import re

with open("input.txt") as f:
    sensors = [[int(n) for n in re.findall(r"-?\d+", s)] for s in f.read().splitlines()]

def dist(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def find_ranges(target_row):
    ranges = []
    for sx, sy, bx, by in sensors:
        d = dist((sx, sy), (bx, by))
        # If target is within sensor
        if sy - d <= target_row <= sy + d:
            dy = abs(sy-target_row)
            ranges.append(sorted((sx-(d-dy), sx+(d-dy))))
    return sorted(ranges)

def count_ranges(ranges, rmin=None, rmax=None):
    ranges = sorted(ranges)
    total = 0
    xmin, xmax = ranges[0]
    if rmin is not None:
        xmin = max(rmin, xmin)
    if rmax is not None:
        xmax = min(rmax, xmax)

    for a, b in ranges[1:]:
        # Overlapping
        if xmax >= a: 
            xmax = max(xmax, b)
            if rmax is not None:
                xmax = min(rmax, xmax)
        else:
            # Ikke overlapp
            print(xmax, a)
            total += xmax - xmin + 1
            xmax = b
            if rmax is not None:
                xmax = min(rmax, b)
            xmin = a
            if rmin is not None:
                xmin = max(rmin, a)
    total += xmax - xmin + 1
    return total

def is_overlap(y):
    ranges = sorted(find_ranges(y))

    xmax = ranges[0][1]
    for start, end in ranges[1:]:
        if xmax < start:
            # Ikke overlapp
            print("Part 2:\t", 4000000*(start-1) + y)
            return False 
        # Overlapping
        xmax = max(xmax, end)
    return True

target_row = 2000000 
bys = set(by for *__, by in sensors)

print("Part 1:\t", count_ranges(find_ranges(target_row)) - sum(by == target_row for by in bys))

# Part 2 does take a couple of minutes
maxes = 4000000
for y in range(maxes+1):
    if not is_overlap(y):
        break
