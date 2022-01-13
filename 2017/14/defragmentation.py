""" Advent of Code 2017. Day 14: Disk Defragmentation """
from re import U
import sys

sys.path.insert(1, "../10")

from hash import knothash

keystring = "flqrgnkx"
keystring = "ugkiagan"


def create_grid(keystring):
    grid = set()
    for i in range(128):
        hexes = knothash("-".join((keystring, str(i))))
        bits = "".join(bin(int(h, 16))[2:].zfill(4) for h in hexes)

        grid.update({(i, j) for j, bit in enumerate(bits) if bit == "1"})
    return grid


grid = create_grid(keystring)
print("Part 1:\t", len(grid))

# let's traverse!
def dfs(x, y, grid):
    stack = [(x, y)]
    seen = set()
    while stack:
        x, y = stack.pop()
        seen.add((x, y))

        stack.extend(
            [
                (x + dx, y + dy)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                if (x + dx, y + dy) not in seen and (x + dx, y + dy) in grid
            ]
        )
    return seen


def floodfill(grid):
    count = 0
    while grid:
        x, y = grid.pop()

        grid -= dfs(x, y, grid)
        count += 1
    return count


print("Part 2:\t", floodfill(grid))

