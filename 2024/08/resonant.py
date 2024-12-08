""" Advent of Code 2024. Day 8: Resonant Collinearity """
from collections import defaultdict
from itertools import combinations

with open("input.txt") as f:
    grid = f.read().splitlines()

xmax = len(grid[0])
ymax = len(grid)


def parse_grid(grid):
    mapgrid = defaultdict(list)
    for y, row in enumerate(grid[::-1]):
        for x, col in enumerate(row):
            if col != ".":
                mapgrid[col].append((x, y))
    return mapgrid


antennas = parse_grid(grid)


def distance(a, b):
    return (a[0] - b[0], a[1] - b[1])


def is_within_bounds(x, y):
    return 0 <= x < xmax and 0 <= y < ymax


def antinode(a, b):
    dx, dy = distance(a, b)
    nodes = []

    x, y = a
    if is_within_bounds(x + dx, y + dy):
        x += dx
        y += dy
        nodes.append((x, y))

    x, y = b
    if is_within_bounds(x - dx, y - dy):
        x -= dx
        y -= dy
        nodes.append((x, y))

    return nodes


antinodes = set()
for frequency in antennas:
    for a, b in combinations(antennas[frequency], 2):
        antinodes.update(antinode(a, b))
print("Part 1:\t", len(antinodes))


def antinode2(a, b):
    dx, dy = distance(a, b)
    nodes = []

    x, y = a
    while is_within_bounds(x + dx, y + dy):
        x += dx
        y += dy
        nodes.append((x, y))

    x, y = b
    while is_within_bounds(x - dx, y - dy):
        x -= dx
        y -= dy
        nodes.append((x, y))

    return nodes


antinodes = set()
for frequency in antennas:
    antinodes.update(antennas[frequency])
    for a, b in combinations(antennas[frequency], 2):
        antinodes.update(antinode2(a, b))
print("Part 2:\t", len(antinodes))
