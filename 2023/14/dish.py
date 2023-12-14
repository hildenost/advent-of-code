""" Advent of Code 2023. Day 14: Parabolic Reflector Dish """


with open("input.txt") as f:
    grid = f.readlines()

testgrid = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".splitlines()

# grid = testgrid


from collections import defaultdict

squares = defaultdict(list)
rowsquares = defaultdict(list)
stones = defaultdict(list)

for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == "#":
            squares[x].append(y)
            rowsquares[y].append(x)
        elif col == "O":
            stones[x].append(y)

size = len(grid)

load = 0
for col in range(size):
    counts = {
        i: sum(i < stone < j for stone in stones[col])
        for i, j in zip([-1] + squares[col], squares[col] + [size])
    }

    load += sum(
        sum(size - c - 1 for c in range(lower, lower + count))
        for lower, count in counts.items()
    )
print("Part 1:\t", load)


def tilt(stones, to="N"):
    # Need to have the stones per tilt axis
    # That is, when tilting north or south, stones are grouped by columns first
    # When tilting west or east, they should be grouped by rows first
    # In other words: alternating
    if to in ["E", "W"]:
        walls = rowsquares
    else:
        walls = squares

    if to in "NW":
        counts = [
            # The variable says col, but it could also be row
            # The tilting works by grouping the stones into separate boxes
            # that is, the gaps between the square stones
            {
                i: sum(i < stone < j for stone in stones[col])
                for i, j in zip([-1] + walls[col], walls[col] + [size])
            }
            for col in range(size)
        ]
    elif to in "ES":
        # Storing the upper limit
        counts = [
            # The variable says col, but it could also be row
            # The tilting works by grouping the stones into separate boxes
            # that is, the gaps between the square stones
            {
                j: sum(i < stone < j for stone in stones[col])
                for i, j in zip([-1] + walls[col], walls[col] + [size])
            }
            for col in range(size)
        ]

    # Then, we know how many are grouped per segment, and consequently,
    # which rows they occupy
    new_index = lambda k, r: k + 1 + r if to in "NW" else k - 1 - r

    new_stones = defaultdict(list)
    for col, count in enumerate(counts):
        for k, v in count.items():
            for r in range(v):
                new_stones[new_index(k, r)].append(col)

    # this new position should be stored in the opposite grouping
    # That is, tilting N-S should store the results for tilting E-W
    return new_stones


def cycle(stones):
    for direction in "NWSE":
        stones = tilt(stones, to=direction)
    return stones


memory = defaultdict(list)
testcycles = 500
for i in range(testcycles):
    stones = cycle(stones)

    if i > testcycles // 2:
        for col in stones:
            memory[col].append(tuple(stones[col]))


def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


for col in memory:
    colset = set(memory[col])

    repeats = [r for r in [indices(memory[col], c) for c in colset] if r]
#    if len(repeats) > 1:
#        print(repeats)

cycles = 1000000000
cycles -= testcycles

# By manual inspection
cycles %= 9

# Doing the additional cycling to get the desired state
for i in range(cycles):
    stones = cycle(stones)

load = sum(sum(size - row for row in stones[col]) for col in stones)
print("Part 2:\t", load)
