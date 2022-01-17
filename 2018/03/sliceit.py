""" Advent of Code 2018. Day 3: No Matter How You Slice It """

with open("input.txt") as f:
    claims = f.read().splitlines()


from math import comb
import re

pattern = re.compile(r"\d+")
squares = {}
for claim in claims:
    id, x, y, w, h = re.findall(pattern, claim)
    squares.update({(int(x), int(x) + int(w), int(y), int(y) + int(h)): id})


def is_overlap(A, B):
    # A/B = xmin, xmax, ymin, ymax
    is_NOT_x_overlap = A[1] < B[0] or A[0] > B[1]
    is_NOT_y_overlap = A[3] < B[2] or A[2] > B[3]
    return not (is_NOT_x_overlap or is_NOT_y_overlap)


def overlap_area(*squares):
    xmin = max(s[0] for s in squares)
    xmax = min(s[1] for s in squares)
    ymin = max(s[2] for s in squares)
    ymax = min(s[3] for s in squares)
    return (xmin, xmax, ymin, ymax)


from itertools import combinations

overlapped_inches = set()
is_not_overlapped = set(squares)
for a, b in combinations(squares, 2):
    if is_overlap(a, b):
        is_not_overlapped.discard(a)
        is_not_overlapped.discard(b)
        xmin, xmax, ymin, ymax = overlap_area(a, b)
        overlapped_inches.update(
            {(x, y) for x in range(xmin, xmax) for y in range(ymin, ymax)}
        )


print("Part 1:\t", len(overlapped_inches))
print("Part 2:\t", squares[is_not_overlapped.pop()])
