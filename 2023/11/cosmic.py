""" Advent of Code 2023. Day 11: Cosmic Expansion """

with open("input.txt") as f:
    universe = f.readlines()

testuniverse = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".splitlines()

# universe = testuniverse


# Find galaxies
def find_galaxies(universe):
    galaxies = set()
    empty_rows = set(range(len(universe)))
    empty_cols = set(range(len(universe[0])))
    for y, row in enumerate(universe):
        for x, col in enumerate(row):
            if col == "#":
                galaxies.add((x, y))
                empty_rows -= {y}
                empty_cols -= {x}
    return galaxies, empty_rows, empty_cols


# Expand rows
def expand(galaxies, empty_rows, empty_cols, factor=2):
    expand_y = {y: sum(y > row for row in empty_rows) for __, y in galaxies}
    expand_x = {x: sum(x > row for row in empty_cols) for x, __ in galaxies}

    return [
        (x + expand_x[x] * (factor - 1), y + expand_y[y] * (factor - 1))
        for x, y in galaxies
    ]


# all pairs shortest path but it's just Manhattan
def dist(a, b):
    """Manhattan distance"""
    return abs(a[1] - b[1]) + abs(a[0] - b[0])


def all_shortest(galaxies):
    return sum(
        sum(dist(galaxy, galaxies[k]) for k in range(i + 1, len(galaxies)))
        for i, galaxy in enumerate(galaxies)
    )


galaxies = expand(*find_galaxies(universe))
answer = all_shortest(galaxies)
print("Part 1:\t", answer)

galaxies = expand(*find_galaxies(universe), factor=1_000_000)
answer = all_shortest(galaxies)
print("Part 2:\t", answer)
