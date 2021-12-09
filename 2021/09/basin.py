""" Advent of Code 2021. Day 9: Smoke Basin """

heightmap = """2199943210
3987894921
9856789892
8767896789
9899965678
""".splitlines()

with open("input.txt") as f:
    heightmap = f.read().splitlines()


risk_level = 0
for j, row in enumerate(heightmap):
    for i, col in enumerate(row):
        if i > 0 and row[i - 1] <= col:
            continue
        if i < len(heightmap[0]) - 1 and row[i + 1] <= col:
            continue
        if j > 0 and heightmap[j - 1][i] <= col:
            continue
        if j < len(heightmap) - 1 and heightmap[j + 1][i] <= col:
            continue

        risk_level += int(row[i]) + 1

print("Part 1:\t", risk_level)


def within_bounds(i, j):
    return 0 <= j < len(heightmap) and 0 <= i < len(heightmap[0])


def count_basin(i, j, visited):
    if (i, j) in visited or not within_bounds(i, j):
        return 0, visited

    visited.add((i, j))

    if heightmap[j][i] == "9":
        return 0, visited

    temp_sum = 0
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        nb, visited = count_basin(i + dx, j + dy, visited)
        temp_sum += nb

    return 1 + temp_sum, visited


visited = set()
basins = []
for j, row in enumerate(heightmap):
    for i, col in enumerate(row):
        basin_size, visited = count_basin(i, j, visited)
        if basin_size:
            basins.append(basin_size)

total = 1
for b in sorted(basins, reverse=True)[:3]:
    total *= b
print("Part 2:\t", total)

