""" Advent of Code 2018. Day 23: Experimental Emergency Teleportation """

import re

with open("input.txt") as f:
    nanobots = [re.findall(r"-?\d+", line) for line in f.read().splitlines()]

# nanobots = [
#    (0, 0, 0, 4),
#    (1, 0, 0, 1),
#    (4, 0, 0, 3),
#    (0, 2, 0, 1),
#    (0, 5, 0, 3),
#    (0, 0, 3, 1),
#    (1, 1, 1, 1),
#    (1, 1, 2, 1),
#    (1, 3, 1, 1),
# ]
#
nanobots = [
    (10, 12, 12, 2),
    (12, 14, 12, 2),
    (16, 12, 12, 4),
    (14, 14, 14, 6),
    (50, 50, 50, 200),
    (10, 10, 10, 5),
]


class Bot:
    def __init__(self, pos, r):
        self.pos = pos
        self.r = r

    def __lt__(self, other):
        return self.r < other.r

    def __eq__(self, other):
        return (self.pos, self.r) == (other.pos, other.r)

    def __hash__(self):
        return hash((self.pos, self.r))

    def __repr__(self):
        return f"Bot({self.pos}, {self.r})"

    def in_bb_range(self, other):
        dist = sum(abs(a - b) for a, b in zip(self.pos, other.pos))
        return dist <= self.r


nanobots = [Bot((int(x), int(y), int(z)), int(r)) for x, y, z, r in nanobots]

largest_bot = max(nanobots)
print("Part 1:\t", sum(largest_bot.in_bb_range(bot) for bot in nanobots))

from itertools import combinations

def is_overlap(bot, other):


def overlap_volume(bot, other):
    minx = max(bot.pos[0] - bot.r, other.pos[0] - other.r)
    maxx = min(bot.pos[0] + bot.r, other.pos[0] + other.r)
    miny = max(bot.pos[1] - bot.r, other.pos[1] - other.r)
    minz = max(bot.pos[2] - bot.r, other.pos[2] - other.r)

    r = (maxx - minx) // 2

    return Bot((minx + r, miny + r, minz + r), r)


# overlapped = set()
# for bot, other in combinations(nanobots, 2):
#    is_overlap = bot.in_bb_range(other) or other.in_bb_range(bot)
#
#    if is_overlap:
#        # find overlapping volume
#        overlapped.add(overlap_volume(bot, other))
#
# print(len(overlapped))


def find_max_overlaps(bot, rest):
    # First we compare with the remaining cuboids in list
    print("GOT ", bot, "\t", rest)
    overlaps = [
        overlap_volume(bot, other)
        for other in rest
        if bot.in_bb_range(other) or other.in_bb_range(bot)
    ]
    print(len(overlaps))
    print(overlaps)

    for i, bot in enumerate(overlaps):
        find_max_overlaps(bot, overlaps[i + 1 :])


#    return +sum(
#        find_max_overlaps(cube, overlaps[i + 1 :]) for i, cube in enumerate(overlaps)
#    )

for i, bot in enumerate(nanobots):
    print()
    print(bot)
    find_max_overlaps(bot, nanobots[i + 1 :])
