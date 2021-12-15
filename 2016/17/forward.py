""" Advent of Code 2016. Day 17: Two Steps Forward """

from hashlib import md5

open_doors = "bcdef"
#               UP      DOWN    LEFT    RIGHT
neighbours = {
        (0, -1): "U",
        (0, 1): "D",
        (-1, 0): "L",
        (1, 0): "R"
}


def reach_vault(passcode, part=1):
    longs = []
    queue = [("", 0, 0)]
    while queue:
        p, x, y = queue.pop(0)

        if (x, y) == (3, 3):
            if part == 1:
                return p 
            if part == 2:
                longs.append(len(p))
                continue

        h = md5((passcode + p).encode()).hexdigest()[:4]
        # up down left right
        dirs = [c in open_doors for c in h]

        queue.extend([(p+neighbours[(dx, dy)], x+dx, y+dy)
            for o, (dx, dy) in zip(dirs, neighbours)
            if o and 0 <= x + dx < 4 and 0 <= y + dy < 4
            ])
    return max(longs)

passcode = "hijkl"
print("Part 1:\t", reach_vault(passcode))
print("Part 2:\t", reach_vault(passcode, part=2))
