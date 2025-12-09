"""Advent of Code 2025. Day 9: Movie Theater"""

with open("input.txt") as f:
    tiles = f.read().splitlines()

example = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".splitlines()
# tiles = example

tiles = [tuple(int(n) for n in row.split(",")) for row in tiles]


from itertools import combinations


def area(p1, p2):
    return (abs(p2[1] - p1[1]) + 1) * (abs(p2[0] - p1[0]) + 1)


areas = [(area(p1, p2), p1, p2) for p1, p2 in combinations(tiles, 2)]

part1 = max(areas)[0]
print("Part 1:\t", part1)


def is_between(a, b, c):
    minx = min(a[0], b[0])
    maxx = max(a[0], b[0])
    miny = min(a[1], b[1])
    maxy = max(a[1], b[1])
    return (
        # Completely inside
        minx < c[0] < maxx
        and miny < c[1] < maxy
    )


def is_green(p):
    """Check inside point of the alleged rectangle is green"""
    # Not completed because I cheesed it by inspecting the input
    # if the point is also in another rectangle
    x, y = p

    print(x, y)
    for a, b in tiles:
        # Checking x-direction to the right
        if a >= x:
            print(a, b, " to the right!")
    pass


def select_point(p1, p2):
    """Return an inner point of rectangle bounded by p1, p2"""
    # Meant to be used with ray casting, but I cheesed it instead
    mid_x = min(p1[0], p2[0]) + abs(p1[0] - p2[0]) // 2
    mid_y = min(p1[1], p2[1]) + abs(p1[1] - p2[1]) // 2
    return mid_x, mid_y


def is_inside(p1, p2):
    # If any other point A exists
    # so that p1[0] < A[0] < p2[0]
    #      or p1[1] < A[1] < p2[1]
    # rectangle is not correct
    for A in tiles:
        if A == p1 or A == p2:
            continue
        if is_between(p1, p2, A):
            return True
    return False


# After plotting, we see that the largest area must be either completely above or below
# ~50000
# Here are the critical points, where suddenly the x-value spikes:
# 94634,50282
# 94634,48476

import matplotlib.pyplot as plt
import numpy as np

# Kun for plotting
np_tiles = np.array(tiles)

for a, p1, p2 in sorted(areas, reverse=True):
    # Check if points on same side of great chunk
    on_same_side = (p1[1] >= 50282 and p2[1] >= 50282) or (
        p1[1] <= 48476 and p2[1] <= 48476
    )
    if on_same_side and not is_inside(p1, p2):
        print("Part 2:\t", a)
        fig, ax = plt.subplots()
        ax.plot(np_tiles[:, 0], np_tiles[:, 1], zorder=0)
        ax.scatter(p1[0], p1[1], marker="s", c="darkred", zorder=5)
        ax.scatter(p2[0], p2[1], marker="s", c="darkred", zorder=5)

        ax.add_patch(
            plt.Rectangle(
                (min(p1[0], p2[0]), min(p1[1], p2[1])),
                width=abs(p1[0] - p2[0]),
                height=abs(p1[1] - p2[1]),
                alpha=0.2,
            )
        )
        plt.show()
        break
