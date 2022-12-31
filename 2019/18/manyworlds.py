""" Advent of Code 2019. Day 18: Many-Worlds Interpretation """

with open("input.txt") as f:
    maze = f.read()

# Gonna represent the walls in a set
# So easy to check whether tile is wall or not
# In addition, keeping a dict of position of doors

# Initialisation
WALLS = set()
DOORS = {}
KEYS = {}
invkeys = {}
for i, row in enumerate(maze.splitlines()):
    for j, tile in enumerate(row):
        if tile == "#":
            WALLS.add((i, j))
        elif tile.isupper():
            DOORS[(i, j)] = tile
        elif tile.islower():
            KEYS[(i, j)] = tile 
            invkeys[tile] = (i, j)
        elif tile == "@":
            poses = ((i, j),)

            # Part 2
            """
            Replacing
            ...    @#@
            .@. -> ### 
            ...    @#@
            """
            poses_2 = tuple(
                (i+di, j+dj)
                for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            )
            EXTRAWALLS = {
                (i+di, j+dj)
                for di, dj in [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
            }

keys = "".join(sorted(KEYS.values()))

from heapq import heappush
from heapq import heappop

# Just doing a naive bfs for finding accessible keys
def bfs(start, sorted_verts="", part=1):
    visited = set()
    queue = [(0, start)]

    cost = {}

    while queue:
        c, pos = queue.pop(0)
        if pos in visited:
            continue

        visited.add(pos)
        # Then we visit the neighbours
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            new_pos = (pos[0] + dx, pos[1] + dy)

            if new_pos in visited:
                continue
            # If deadend
            if new_pos in WALLS or DOORS.get(new_pos, "Ø").lower() in sorted_verts:
                continue

            if part == 2 and new_pos in EXTRAWALLS:
                continue

            # If key, add cost to key, but skip the rest
            if KEYS.get(new_pos, "ø") in sorted_verts:
                cost[KEYS[new_pos]] = c + 1
                continue

            queue.append((c+1, new_pos))
    return cost

def keysearch(keys, starts, part=1):
    # A state should contain the vertices left, the unlocked doors
    # (cost, keys, poses)
    queue = []
    heappush(queue, (0, keys, starts))
    visited = set()

    while queue:
        cost, vertices, poses = heappop(queue)
        
        state = (vertices, poses)

        if state in visited:
            continue

        visited.add(state)

        if len(vertices) == 0:
            print(f"Explored {len(visited)} nodes")
            return cost

        # let's find the reachable keys from pos
        dists = [bfs(pos, vertices, part) for pos in poses]

        for i, dist in enumerate(dists):
            for v in dist:
                # Opening doors and updating pos
                new_poses = poses[:i] + (invkeys[v],) + poses[i+1:]
                state = (vertices.replace(v, ""), new_poses)

                if state in visited:
                    continue

                # If we visit this key first, let's add to queue
                heappush(queue, (cost + dist[v], *state))

print("Part 1:\t", keysearch(keys, tuple(poses)))
print("Part 2:\t", keysearch(keys, tuple(poses_2), part=2))

