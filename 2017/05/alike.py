""" Advent of Code 2017. Day 5: A Maze of Twisty Trampolines, All Alike """


def maze(limit=None):
    with open("input.txt") as f:
        offsets = [int(line) for line in f.read().splitlines()]

    if limit is None:
        limit = len(offsets)

    n = 0
    p = 0
    while p < len(offsets):
        new_p = p + offsets[p]
        offsets[p] += 1 if offsets[p] < limit else -1
        p = new_p

        n += 1

    return n


print("Part 1:\t", maze())
print("Part 2:\t", maze(limit=3))
