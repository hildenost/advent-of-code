""" Advent of Code 2020 Day 17: Conway Cubes """
from collections import defaultdict
from itertools import product

# x -->
# y
# |
# |
# v
initial_state = """\
.#.
..#
###
"""
initial_state = """\
#.#..#.#
#.......
####..#.
.#.#.##.
..#..#..
###..##.
.#..##.#
.....#..
"""


def count_neighbours(cube, coord, directions):
    return sum(
        cube.get(tuple(sum(pair) for pair in zip(dirs, coord)), False)
        for dirs in directions
    )


def get_changed_state(cube, directions):
    changed_states = defaultdict(str)
    for coord in cube:
        n = count_neighbours(cube, coord, directions)
        if cube[coord] and n not in [2, 3]:
            changed_states[coord] = False
        elif not cube[coord] and n == 3:
            changed_states[coord] = True
    return changed_states


def pprint(cube, cycle=None):
    dims = len(list(cube.keys())[0])

    # Create list of coordinates in cube
    lower, upper = min(cube), max(cube)
    coords = product(*[range(low, high + 1) for low, high in zip(lower, upper)])
    # Sorting them so that the w coordinate grows first, z second,
    # but x, y kept in original order
    if len(lower) > 3:
        coords = sorted(coords, key=lambda c: (c[3], c[2]))
    elif len(lower) > 2:
        coords = sorted(coords, key=lambda c: c[2])

    out = ""
    curr_row = None
    curr_z = None

    for x, y, *rest in coords:
        if len(rest) and rest[0] != curr_z:
            curr_z = rest[0]
            out += f"\n\nz={curr_z}"
            if len(rest) > 1:
                out += f", w={rest[1]}"

        if x != curr_row:
            out += "\n"
            curr_row = x
        out += "#" if cube[(x, y, *rest)] else "."
    print(out)


def expand_view(cube):
    # Create list of coordinates in cube
    lower, upper = min(cube), max(cube)
    coords = product(*[range(low - 1, high + 2) for low, high in zip(lower, upper)])
    return {coord: cube.get(coord, False) for coord in coords}


def initialise(initial_state, dims=3):
    if dims < 2:
        print("No can do. Dimension has to be at least 2D.")
        return
    zeroes = tuple([0] * (dims - 2))
    directions = {coord for coord in product([0, 1, -1], repeat=dims)}
    directions.remove(tuple([0] * dims))
    return (
        {
            (i, j, *zeroes): x == "#"
            for j, l in enumerate(initial_state.splitlines())
            for i, x in enumerate(l)
        },
        directions,
    )


def run_simulation(initial_state, dims=3, cycles=6, verbose=False):
    conway_cube, directions = initialise(initial_state, dims=dims)

    for c in range(cycles):
        if verbose:
            pprint(conway_cube)
        conway_cube = expand_view(conway_cube)
        conway_cube.update(get_changed_state(conway_cube, directions))

    return conway_cube


def solve(initial_state, part=1):
    dims_dict = {1: 3, 2: 4}
    final_state = run_simulation(initial_state, dims_dict[part])
    print(f"Part {part}: {sum(final_state.values())}")


solve(initial_state, part=1)
solve(initial_state, part=2)
