""" Advent of Code 2019 Day 24: Planet of Discord """

state = """....#
#..#.
#..##
..#..
#....
"""

state = """##...
#.###
.#.#.
#....
..###
"""
BUG = "#"
EMPTY = "."
EMPTYSTATE = EMPTY * 25


def parse_input(state, part=1):
    state = "".join(state.splitlines())
    if part == 2:
        return state

    state = "".join("1" if c == BUG else "0" for c in state)
    return int(state, 2)


def pprint(binary):
    print()
    string = f"{binary:025b}"
    for row in range(5):
        print(
            "".join(BUG if c == "1" else EMPTY for c in string[5 * row : 5 * (row + 1)])
        )


def bitmask(k):
    neighbours = [
        k - 5,  # UP
        k - 1 if k % 5 else -1,  # LEFT except when left edge
        k + 1 if k % 5 != 4 else -1,  # RIGHT except when right edge
        k + 5,  # DOWN
    ]
    bitstring = "".join("1" if c in neighbours else "0" for c in range(25))
    return int(bitstring, 2)


BITMASK = {k: bitmask(k) for k in range(25)}

RULES = {
    "0": lambda bugs: str(int(bugs in (1, 2))),
    "1": lambda bugs: str(int(bugs == 1)),
}


def update(state):
    return int(
        "".join(
            RULES[f"{state:025b}"[k]](f"{(BITMASK[k] & state):b}".count("1"))
            for k in range(25)
        ),
        2,
    )


def score(state):
    return sum(2**k for k, cell in enumerate(f"{state:025b}") if cell == "1")


def part1(state):
    state = parse_input(state)
    seen = {state}
    while True:
        state = update(state)

        if state in seen:
            return score(state)

        seen.add(state)


print("Part 1:\t", part1(state))


def print_state(state, part=1):
    """Pretty print the state string as a 5x5 grid"""
    print()
    for row in range(5):
        print(state[5 * row : 5 * (row + 1)])


def has_bug(state, k):
    # Special case when k = 12
    return state[k] == BUG and k != 12


# Special tiles are the ones in part 1 (edges)
# in addition to the new ones:
# - middle tile is a grid level up
# - the neighbours of the middle tile (7, 11, 13, 17)
ranges = {
    7: range(5),  # All upper edge a level up
    11: range(0, 25, 5),  # All left edge a level up
    13: range(4, 25, 5),  # All right edge a level up
    17: range(20, 25, 1),  # All lower edge a level up
}

DIM = 5
DIM2 = DIM * DIM
MID = DIM2 // 2
MIDNEIGHBOURS = [MID + c for c in (1, -1, DIM, -DIM)]

edges = {
    "UPPER": range(DIM),
    "LEFT": range(0, DIM2, DIM),
    "RIGHT": range(DIM - 1, DIM2, DIM),
    "LOWER": range(DIM2 - DIM, DIM2, 1),
}

ranges = {
    MID + c: range(*sets)
    for c, sets in [
        (1, (DIM - 1, DIM2, DIM)),
        (-1, (0, DIM2, DIM)),
        (DIM, (DIM2 - DIM, DIM2, 1)),
        (-DIM, (0, DIM, 1)),
    ]
}


def count_bugs(grid, k, level=0):
    bugs = 0

    # Special cases
    # The MIDDLE tile
    # Is skipped in another layer, but let's just keep it for now
    if k == 12:
        return bugs

    # The neighbours of the MIDDLE tile
    if k in ranges:
        bugs += sum(has_bug(grid.get(level + 1, EMPTYSTATE), c) for c in ranges[k])

    # UPPER neighbours
    # on uppermost edge, neighbour is k=7 a level DOWN from current level
    bugs += (
        has_bug(grid.get(level - 1, EMPTYSTATE), k=7)
        if k in edges["UPPER"]
        else has_bug(grid.get(level, EMPTYSTATE), k=k - 5)
    )

    # LOWER neighbours
    # on lowermost edge, neighbour is k=17 a level DOWN from current level
    bugs += (
        has_bug(grid.get(level - 1, EMPTYSTATE), k=17)
        if k in edges["LOWER"]
        else has_bug(grid.get(level, EMPTYSTATE), k=k + 5)
    )

    # LEFT neighbours
    # on leftmost edge, neighbour is k=11 a level DOWN from current level
    bugs += (
        has_bug(grid.get(level - 1, EMPTYSTATE), k=11)
        if k in edges["LEFT"]
        else has_bug(grid.get(level, EMPTYSTATE), k=k - 1)
    )

    # RIGHT neighbours
    # on rightmost edge, neighbour is k=13 a level DOWN from current level
    bugs += (
        has_bug(grid.get(level - 1, EMPTYSTATE), k=13)
        if k in edges["RIGHT"]
        else has_bug(grid.get(level, EMPTYSTATE), k=k + 1)
    )

    return bugs


def apply(grid, k, level=0):
    bugs = count_bugs(grid, k, level)

    if has_bug(grid[level], k) and bugs == 1:
        return BUG

    if not has_bug(grid[level], k) and bugs in [1, 2]:
        return BUG

    return EMPTY


def new_state(grid, level=0):
    if level not in grid:
        grid[level] = EMPTYSTATE

    return "".join(apply(grid, k, level) if k != 12 else "?" for k in range(25))


def part2(state):
    state = parse_input(state, part=2)
    grid = dict()
    grid[0] = state
    for __ in range(200):
        max_level = max(grid.keys()) + 1
        min_level = min(grid.keys()) - 1

        grid = {
            level: new_state(grid, level) for level in range(min_level, max_level + 1)
        }
    return sum(state.count(BUG) for state in grid.values())


print("Part 2:\t", part2(state))
