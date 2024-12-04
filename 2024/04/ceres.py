""" Advent of Code 2024. Day 4: Ceres Search """

with open("input.txt") as f:
    grid = [l for l in f.read().splitlines()]

neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

# grid = """\
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """.splitlines()

total = 0
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == "X":
            # Search for XMAS
            for di, dj in neighbours:
                if i + 3 * di >= len(grid) or j + 3 * dj >= len(row):
                    continue
                if i + 3 * di < 0 or j + 3 * dj < 0:
                    continue
                word = (
                    char
                    + grid[i + di][j + dj]
                    + grid[i + 2 * di][j + 2 * dj]
                    + grid[i + 3 * di][j + 3 * dj]
                )
                # print(word)
                if word == "XMAS":
                    total += 1
print("Part 1:\t", total)

neighbours = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
total = 0
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == "A":
            # Search for X-MAS
            # Checking if the letters surrounding A diagonally
            # are 2 S og 2 M
            letters = []
            for di, dj in neighbours:
                if i + di >= len(grid) or j + dj >= len(row):
                    continue
                if i + di < 0 or j + dj < 0:
                    continue
                letters.append(grid[i + di][j + dj])
            if len(letters) == 4:
                if (letters[0], letters[2]) in [("M", "S"), ("S", "M")]:
                    if (letters[1], letters[3]) in [("M", "S"), ("S", "M")]:
                        total += 1
print("Part 2:\t", total)
