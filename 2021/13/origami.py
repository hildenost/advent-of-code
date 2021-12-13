""" Advent of Code 2021. Day 13: Transparent Origami """

instructions = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
with open("input.txt") as f:
    instructions = f.read()

dots, fold = instructions.split("\n\n")

dots = {tuple(int(d) for d in dot.split(",")) for dot in dots.splitlines()}


def horizontal_flip(x, y, line):
    return (x, y) if y < line else (x, line - (y - line))


def vertical_flip(x, y, line):
    return (x, y) if x < line else (line - (x - line), y)


for i, f in enumerate(fold.splitlines()):
    axis, n = f.split()[-1].split("=")

    if axis == "x":
        dots = {vertical_flip(x, y, int(n)) for x, y in dots}
    elif axis == "y":
        dots = {horizontal_flip(x, y, int(n)) for x, y in dots}

    if i == 0:
        print("Part 1:\t", len(dots))


dots = list(dots)
xs, ys = list(zip(*dots))

grid = [[" " for __ in range(max(xs) + 1)] for __ in range(max(ys) + 1)]
for x, y in dots:
    grid[y][x] = "#"

print("Part 2:")
for row in grid:
    print("".join(row))
