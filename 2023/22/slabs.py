""" Advent of Code 2023. Day 22: Sand Slabs """
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def get_max(points, axis=0):
    return max(max(p[axis], p[axis + 3]) for p in points)


def plot_slabs(slabs):
    maxes = tuple(get_max(slabs, i) + 1 for i in range(3))

    aspect = tuple(x / max(maxes) for x in maxes)

    voxels = np.zeros(maxes, dtype=bool)

    for x1, y1, z1, x2, y2, z2 in slabs:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    voxels[x, y, z] = True

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_box_aspect(aspect=aspect)

    ax.voxels(voxels)
    plt.show()


from collections import defaultdict
import re

with open("input.txt") as f:
    slabs = f.read().splitlines()


slabs = [tuple(int(n) for n in re.findall(r"\d+", line)) for line in slabs]


# Let's walk through layer by layer
# Each "floor" is only 10x10


def settle_bricks(slabs):
    # Sorting by z
    slabs = sorted(slabs, key=lambda x: (x[2], x[5]))

    new_slabs = []
    floors = defaultdict(set)

    for x1, y1, z1, x2, y2, z2 in slabs:
        delta_z = z2 - z1

        xys = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]

        # First, check whether the floors below have
        # space for the slabs
        # Only the lowest valued z is necessary
        for z in range(z1, 0, -1):
            is_space = all((x, y) not in floors[z] for x, y in xys)
            if not is_space:
                # No room at this level
                # Quit loop and backtrack up 1 level
                z += 1
                break

        # Second, update the floor with the new footprint
        for new_z in range(z, z + delta_z + 1):
            for x, y in xys:
                floors[new_z].add((x, y))

        # Third, store the new slab positions
        new_slabs.append((x1, y1, z, x2, y2, z + delta_z))

    return new_slabs


slabs = settle_bricks(slabs)

# Let's find out who supports who
floors = defaultdict(set)
# Store the slabs in their respective floors
# Only the lowest z is needed
for slab in slabs:
    floors[slab[2]].add(slab)


supports = defaultdict(list)
is_supported_by = defaultdict(list)

for i, (x1, y1, z1, x2, y2, z2) in enumerate(slabs):
    # Are there any slabs on the floor above?
    for slab in floors[z2 + 1]:
        if x1 <= slab[3] and x2 >= slab[0] and y1 <= slab[4] and y2 >= slab[1]:
            # Intersection
            j = slabs.index(slab)
            supports[i].append(j)
            is_supported_by[j].append(i)


# Disintegrating bricks
# 1. Bricks that do not support other bricks, can be disintegrated
no_supports = sum(n not in supports for n in range(len(slabs)))
# 2. Bricks that support another brick together with at least one other brick, can be disintegrated
disintegratable = set()
impossibles = set()
for bricks in is_supported_by.values():
    if len(bricks) > 1:
        disintegratable.update(bricks)
    else:
        impossibles.update(bricks)

# NB! Some bricks might share the responsibility of supporting a brick, but might still be alone in supporting another
# We should remove them from the disintegratable set
disintegratable -= impossibles
print("Part 1:\t", len(disintegratable) + no_supports)


# Now it's time for the traversal up the other way
# Though, a particular brick cannot fall unless _all_ its supports are marked for falling
# Consequently, this is a job for bfs


def bfs(brick):
    # Marking the current brick
    marked = {brick}

    # Enqueuing the children of the brick
    queue = supports.get(brick, [])

    while queue:
        new_queue = set()
        for b in queue:
            # If all supports of the current brick b is falling,
            # the current brick will also fall
            if set(is_supported_by[b]) <= marked:
                marked.add(b)
                new_queue.update(supports[b])
        queue = new_queue

    # The count of falling bricks is exclusive so subtracting the root
    return len(marked) - 1


print("Part 2:\t", sum(bfs(brick) for brick in impossibles))
