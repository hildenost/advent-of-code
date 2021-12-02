import re

with open("06/input.txt") as f:
    lines = f.read().splitlines()

grid = [[False] * 1000] * 1000

INSTRUCTIONS = {
    "turn on": lambda x: True,
    "turn off": lambda x: False,
    "toggle": lambda x: x ^ True,
}


def config_lights(cmd, lower_i, lower_j, upper_i, upper_j, grid):
    for i in range(int(lower_i), int(upper_i) + 1):
        for j in range(int(lower_j), int(upper_j) + 1):
            grid[i][j] = INSTRUCTIONS[cmd](grid[i][j])
    return grid


pattern = re.compile(
    r"""(?P<cmd>turn on|toggle|turn off) (?P<lower_i>\d+),(?P<lower_j>\d+) through (?P<upper_i>\d+),(?P<upper_j>\d+)"""
)
instructions = (pattern.match(line).groups() for line in lines)

### PART 1
# grid = [[False] * 1000 for __ in range(1000)]
# for cmd, *coords in instructions:
#    grid = config_lights(cmd, *coords, grid)
# print(sum(sum(row) for row in grid))

### PART 2
INSTRUCTIONS = {
    "turn on": lambda x: x + 1,
    "turn off": lambda x: max(x - 1, 0),
    "toggle": lambda x: x + 2,
}


def config_lights(cmd, lower_i, lower_j, upper_i, upper_j, grid):
    for i in range(int(lower_i), int(upper_i) + 1):
        for j in range(int(lower_j), int(upper_j) + 1):
            grid[i][j] = INSTRUCTIONS[cmd](grid[i][j])
    return grid


grid = [[0] * 1000 for __ in range(1000)]
for cmd, *coords in instructions:
    grid = config_lights(cmd, *coords, grid)
print(sum(sum(row) for row in grid))

