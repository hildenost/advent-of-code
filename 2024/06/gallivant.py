""" Advent of Code 2024. Day 6: Guard Gallivant """


grid = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".splitlines()

with open("input.txt") as f:
    grid = f.read().splitlines()

imax = len(grid)
jmax = len(grid[0])


def pprint(grid, visited, obstacle=None):
    for i in range(imax - 1, -1, -1):
        row = ""
        for j in range(jmax):
            if obstacle is not None and obstacle in grid:
                row += "O"
            elif (i, j) in grid:
                row += "#"
            elif (i, j) in visited:
                row += "X"
            else:
                row += "."
        print(row)


def parse_grid(grid):
    mapgrid = set()
    guard = None
    for i, row in enumerate(grid[::-1]):
        for j, col in enumerate(row):
            if col == "#":
                mapgrid.add((i, j))
            elif col in "<>^v":
                guard = (i, j, col)
    return guard, mapgrid


step_forward = {
    "<": lambda y, x: (y, x - 1),
    ">": lambda y, x: (y, x + 1),
    "v": lambda y, x: (y - 1, x),
    "^": lambda y, x: (y + 1, x),
}
turn_90 = {
    "<": "^",
    ">": "v",
    "v": "<",
    "^": ">",
}


def move_guard(guard, grid):
    i, j, direction = guard

    new_pos = step_forward[direction](i, j)

    # No obstacles, let's move!
    if new_pos not in grid:
        return *new_pos, direction

    # Obstacles, let's turn
    return i, j, turn_90[direction]


guard, grid = parse_grid(grid)
starti, startj, startd = guard
visited = set()
visited.add((guard[:2]))

while True:
    i, j, direction = guard
    if i < 0 or j < 0 or i >= imax or j >= jmax:
        # Moving out of bounds ...
        break
    visited.add((i, j))
    guard = move_guard(guard, grid)

print("Part 1:\t", len(visited))

# Possible obstruction spots: the visited spots except starting pos
cycles = 0
for y, x in visited:
    guard = starti, startj, startd
    if (y, x) == guard[:2]:
        # Guard starting position, continue
        continue
    # Add obstacle
    testgrid = grid.copy()
    testgrid.add((y, x))

    visited = set()
    twice = set()

    # Cycle detected when position in twice
    while True:
        i, j, direction = guard
        if i < 0 or j < 0 or i >= imax or j >= jmax:
            # Moving out of bounds ...
            break
        if (i, j, direction) in twice:
            # print("Cycle detected.")
            cycles += 1
            break
        if (i, j) in visited:
            twice.add((i, j, direction))
        visited.add((i, j))
        guard = move_guard(guard, testgrid)
    # pprint(grid, visited, obstacle=(y, x))
print("Part 2:\t", cycles)
