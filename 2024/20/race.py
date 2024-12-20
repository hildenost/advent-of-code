""" Advent of Code 2024. Day 20: Race condition """
inputmap = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".splitlines()

with open("input.txt") as f:
    inputmap = f.read().splitlines()


def parsemap(inputmap):
    walls = set()
    for i, line in enumerate(inputmap):
        for j, cell in enumerate(line):
            if cell == "S":
                start = (j, i)
            elif cell == "E":
                end = (j, i)
            elif cell == "#":
                walls.add((j, i))
    return walls, start, end


walls, start, end = parsemap(inputmap)

ymax = len(inputmap)
xmax = len(inputmap[0])


def is_within_bounds(x, y):
    return 0 <= x < xmax and 0 <= y < ymax


def neighbours(x, y):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return [(x + dx, y + dy) for dx, dy in dirs]


from collections import namedtuple

Node = namedtuple("Node", "x y cost path")


def dijkstra(start, end):
    visited = dict()

    startnode = Node(*start, 0, [start])

    queue = [startnode]

    visited[(startnode.x, startnode.y)] = 0

    while queue:
        n = queue.pop(0)

        if (n.x, n.y) == end:
            return n.cost, n.path

        for x, y in neighbours(n.x, n.y):
            if (x, y) in walls:
                continue

            new_cost = n.cost + 1

            if (x, y) in visited and new_cost >= visited[(x, y)]:
                # Been here
                continue

            visited[(x, y)] = new_cost

            new_node = Node(x, y, new_cost, n.path + [(x, y)])
            queue.append(new_node)
    return visited.get(end)


# Get best time and best path
best, track = dijkstra(start, end)

track = {tile: i for i, tile in enumerate(track)}

from itertools import combinations

print("... this will take roughly 25 secs ... ")

n_saves = 0
n_saves_old = 0
for start, end in combinations(track, 2):
    # No point in exploring when dist > 20
    dist = abs(end[1] - start[1]) + abs(end[0] - start[0])
    if dist > 20:
        continue

    i = track[start]
    j = track[end]
    saved = j - i - dist

    if saved >= 100:
        n_saves += 1

        if dist == 2:
            n_saves_old += 1

print("Part 1:\t", n_saves_old)
print("Part 2:\t", n_saves)
