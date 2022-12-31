""" Advent of Code 2019. Day 18: Many-Worlds Interpretation """

# Walks like astar, talks like astar

sample = """########
#b.A.@.a#
#########
"""
sample = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""
sample = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
"""

sample = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
"""

sample = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
"""

with open("input.txt") as f:
    sample = f.read()

# Gonna represent the walls in a set
# So easy to check whether tile is wall or not
# In addition, keeping a dict of position of doors
# Removing the door positions from the wall set as they are unlocked

# Initialisation
WALLS = set()
doors = {}
DOORS = {}
KEYS = {}
invkeys = {}
for i, row in enumerate(sample.splitlines()):
    for j, tile in enumerate(row):
        if tile == "#":
            WALLS.add((i, j))
        elif tile.isupper():
            doors[tile] = (i, j)
            DOORS[(i, j)] = tile
        elif tile.islower():
            KEYS[(i, j)] = tile 
            invkeys[tile] = (i, j)
        elif tile == "@":
            pos = (i, j)


# Just doing a naive bfs
keys = "".join(sorted(KEYS.values()))
doorses = "".join(sorted(DOORS.values()))

from heapq import heappush
from heapq import heappop

def bfs(start, locked_doors="", sorted_verts=""):

    visited = set()
    queue = [(0, start)]

    cost = {}

    while queue:
        c, pos = heappop(queue)
        if pos in visited:
            continue

        visited.add(pos)
        # Then we visit the neighbours
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            new_pos = (pos[0] + dx, pos[1] + dy)

            if new_pos in visited:
                continue
            # If deadend
            if new_pos in WALLS or DOORS.get(new_pos, "Ø") in locked_doors:
                continue
            # If key, add cost to key, but skip the rest
            if KEYS.get(new_pos, "ø") in sorted_verts:
                cost[KEYS[new_pos]] = c + 1
                continue

            queue.append((c+1, new_pos))
    return cost


def keysearch(keys, doorses, start):
    # A state should contain the vertices left, the unlocked doors
    # (cost, vertices, locked_doors)
    queue = []
    heappush(queue, (0, keys, doorses, start))
    visited = {} 

    i = 0
    while queue:
        i+=1
        cost, vertices, locked_doors, pos = heappop(queue)
        
        if i % 1000 == 0:
            print(cost, len(visited), len(queue), vertices, locked_doors)

        state = (vertices, locked_doors, pos)

        if state in visited:
            continue

        visited[state] = cost

        if len(vertices) == 0:
            return cost

        # let's find the reachable keys from pos
        dists = bfs(pos, locked_doors, vertices)

        for v in dists:
            # Opening doors 
            state = (vertices.replace(v, ""), locked_doors.replace(v.upper(), ""), invkeys[v])

            if state in visited:
                continue

            # If we visit this key first, let's add to queue
            heappush(queue, (cost + dists[v], *state))

print("Part 1:\t", keysearch(keys, doorses, pos))
