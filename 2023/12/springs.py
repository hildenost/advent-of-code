""" Advent of Code 2023. Day 12: Hot Springs """
import re

with open("input.txt") as f:
    records = [row.split() for row in f.readlines()]


def partition(s, k):
    if not k:
        yield [s]
        return
    for i in range(len(s) + 1):
        for tail in partition(s[i:], k - 1):
            yield [s[:i]] + tail


###
# Generate all options for the result and check if they fit
def naive_part1(records):
    counter = 0
    for springs, counts in records:
        # Turning the record into a regex pattern
        springs = springs.replace(".", " ").replace("?", ".")
        pattern = re.compile(springs)

        counts = [int(n) for n in counts.split(",")]

        defects = ["#" * c for c in counts]

        # How many dots (or spaces) must we pad with?
        n_dots = len(springs) - sum(counts)
        dots = " " * n_dots
        # How to split the dots in different combos
        dots_part = partition(dots, len(defects))

        res = [None] * (1 + 2 * len(defects))
        res[1::2] = defects
        for i, part in enumerate(dots_part, 1):
            if not all(c for c in part[1:-1]):
                continue
            # Merging in the dots (or spaces)
            res[::2] = part
            trial = "".join(res)
            if len(trial.split()) == len(counts) and pattern.match(trial) is not None:
                counter += 1
    return counter


# print("Part 1:\t", naive_part1(records))

import math


def place(group, count):
    """How many placement options of length count in group"""
    if group[0] == "#" or group[-1] == "#":
        # If the group is fixed to either side
        # Only one placement option
        return 1
    elif group.count("#") == count:
        # No other options, it is already placed
        return 1
    else:
        i = group.find("#")
        c = group.count("#")
        offset = count - c
        possible = group[i - offset : i + offset + 1]
        print(
            i,
            c,
            count,
            possible,
            len(possible),
            group,
            "\t=>\t",
            math.comb(len(possible), count),
            math.comb(len(possible) - 1, count + 1),
            math.comb(len(possible) - 1, count - 1),
            " options",
        )

    return 0


for springs, counts in records:
    counts = [int(n) for n in counts.split(",")]

    required = sum(counts) + len(counts) - 1
    actual = len(springs)
    print(springs, counts, required, actual)

    groups = [s for s in springs.split(".") if s]
    print(groups)

    for group in groups:
        print("\t", group)

    # STEP 1:
    # Populate the fixed/known defects
    if required == actual:
        print("FITS PERFECT, also no one ever ends up here")
    elif len(groups) == len(counts):
        print("EQUAL AMOUNTS OF GROUPS! meaning one group per count")
        # Special case: a # in each group
        if all("#" in g for g in groups):
            print("A # per group")
            total = 1
            for group, count in zip(groups, counts):
                c = place(group, count)
                print(group, count, c)
                total *= c

    #        for group, count in zip(groups, counts):
    #            print(group, count)
    input()
