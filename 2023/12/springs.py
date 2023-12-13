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
    answers = []
    for springs, counts in records:
        s = 0
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
                s += 1
        counter += s
        answers.append(s)
    return counter, answers


ans, answers = naive_part1(records)
print("Part 1:\t", ans)

import math
from itertools import combinations

# Let's do dynamic programming


A = dict()


def poses(length, bitesize):
    if bitesize > length:
        return 0
    return length - bitesize + 1


def compute_options(group, counts, r):
    options = 0
    for k in range(len(group)):
        if group[k] == ".":
            continue

        i = k + 1 + counts[0]
        first, rest = group[k:i], group[i:]
        last_round = first[0] == "#"

        if first[-1] == "#":
            if last_round:
                break

            continue

        if any(f == "." for f in first[:-1]):
            if last_round:
                break
            continue

        if len(rest) < sum(counts[1:]) + len(counts[1:]) - 1:
            # Not a valid option, aborting the remaining tries
            break

        test = count(rest, counts[1:], r + 1)
        # Saving it all for later
        A[(rest, tuple(counts[1:]))] = test

        options += test
        if first[0] == "#":
            break
    return options


def count(group, counts, r=0):
    # Let's remove the beginning and ending dots
    group = group.strip(".")

    if len(group) < sum(counts) + len(counts) - 1:
        # Not enough room, aborting
        return 0

    if not counts and "#" in group:
        # Error, aborting
        return 0

    if not counts:
        # Nothing to fit, viable option
        return 1

    if group[0] == "#":
        # Special case: Fixed position
        # If all counts can fit
        # set aside the solution and continue
        # Slice the necessary characters and recurse
        first, *rest = group.split(".")
        if len(first) < counts[0]:
            return 0

        if len(group) > counts[0] and group[counts[0]] == "#":
            return 0
        return count(group[counts[0] + 1 :], counts[1:], r + 1)

    if "#" not in group:
        # Special case: All question marks
        if len(counts) == 1:
            # Only 1 count left, base case
            return sum(poses(len(g), counts[0]) for g in group.split("."))

        if (group, tuple(counts)) in A:
            # Been here before, looking it up
            options = A[(group, tuple(counts))]
        else:
            options = compute_options(group, counts, r + 1)

            # Saving it all for later
            A[(group, tuple(counts))] = options

        return options

    # Test whether next group is at the next #
    if len(counts) < 2:
        # print("Only 1 option with ", group, counts)
        # print("Is the solution feasible, though?")
        # TODO memoize
        spans = group.split(".")

        temp = [s for s in spans if "#" in s]
        if len(temp) > 1:
            return 0

        group = temp[0]

        if len(group) < counts[0]:
            return 0

        span = group.rfind("#") - group.find("#") + 1
        if span <= counts[0]:
            if group[0] == "#" or group[-1] == "#":
                return 1
            elif group.count("#") == counts[0]:
                return 1

            left = max(0, group.rfind("#") - counts[0] + 1)
            right = min(group.find("#") + counts[0], len(group))
            group = group[left:right]

            return poses(len(group), counts[0])

        return 0

    if (group, tuple(counts)) in A:
        # Been here before, looking it up
        options = A[(group, tuple(counts))]
    else:
        options = compute_options(group, counts, r + 1)
        A[(group, tuple(counts))] = options
    return options


total = 0
for i, (springs, counts) in enumerate(records):
    counts = [int(n) for n in counts.split(",")]

    counts = 5 * counts
    springs = "?".join([springs] * 5)

    total += count(springs, counts)
print("Part 2:\t", total)
