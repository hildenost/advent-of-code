""" Advent of Code 2018. Day 18: Settlers of The North Pole """
import numpy as np
from scipy.signal import convolve

state = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.
""".splitlines()

with open("input.txt") as f:
    state = f.read().splitlines()

dim = len(state)

trees = np.zeros((dim, dim), dtype=int)
lumberyards = np.zeros((dim, dim), dtype=int)

for i, row in enumerate(state):
    for j, col in enumerate(row):
        trees[i, j] = col == "|"
        lumberyards[i, j] = col == "#"

def draw(yards, trees):
    dim = yards.shape[0]

    print()
    for i in range(dim):
        row = ""
        for j in range(dim):
            if yards[i, j]:
                row += "#"
            elif trees[i, j]:
                row += "|"
            else:
                row += "."
        print(row)
    print()

# The convolution matrix
# 1 1 1
# 1 0 1
# 1 1 1
# Sums the neighbours
B = np.ones((3, 3), dtype=int)
B[1, 1] = 0

def change_state(lumberyards, trees):
    # Convolve counts the occurrence of the neighbours
    surrounding_trees = convolve(trees, B, mode="same")
    surrounding_yards = convolve(lumberyards, B, mode="same")

    new_trees = ~trees & ~lumberyards & (surrounding_trees >= 3)
    new_yards = trees & (surrounding_yards >= 3)

    remaining_trees = trees & (surrounding_yards < 3)
    remaining_yards = lumberyards & (surrounding_trees >= 1) & (surrounding_yards >= 1)

    lumberyards = new_yards | remaining_yards
    trees = new_trees | remaining_trees

    return new_yards | remaining_yards, new_trees | remaining_trees

seen = set()
resource_values = {}
LIMIT = 1_000_000_000
for m in range(1, LIMIT + 1):
    lumberyards, trees = change_state(lumberyards, trees)

    if m == 10:
        print("Part 1:\t", lumberyards.sum() * trees.sum())

    # Storing the state as a tuple
    hashable = tuple(map(tuple,lumberyards * 2 + trees))
    if hashable not in seen:
        seen.add(hashable)
    else:
        #draw(lumberyards, trees)
        # Storing the resource value and minutes
        # AFTER hitting the repetetive, infinte state
        new_value = lumberyards.sum()*trees.sum()

        if new_value in resource_values.values():
            break
        resource_values[m] = new_value

# Removing the minutes before repetition started
# And taking the modulo to get the relative minute from
# the first minute repetition started
equivalent_minute = (1_000_000_000 - min(resource_values)) % len(resource_values)

print("Part 2:\t", resource_values[min(resource_values) + equivalent_minute])
