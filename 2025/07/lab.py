""" Advent of Code 2025. Day 7: Laboratories """

with open("input.txt") as f:
    manifolds = f.read().splitlines()

example = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".splitlines()
#manifolds = example


splitters = {
    (i, j)
    for i, row in enumerate(manifolds)
    for j, col in enumerate(row)
    if col == "^"
}

imax = len(manifolds)

from collections import defaultdict
nodes = defaultdict(list)


start = min(splitters)
queue = [start]
visited = set()

while queue:
    i, j = queue.pop()

    if (i, j) in visited:
        # already beaming here
        continue
    visited.add((i, j))

    # Finding children
    has_left = False
    has_right =False
    for k in range(i+2, imax, 2):
        if not has_right and (k, j+1) in splitters:
            has_right = True
            nodes[(i, j)].append((k, j+1))
            queue.append((k, j+1))

        if not has_left and (k, j-1) in splitters:
            has_left = True
            nodes[(i, j)].append((k, j-1))
            queue.append((k, j-1))

        if has_left and has_right:
            break

print("Part 1:\t",  len(visited))

cache = {}

def count_paths(node):
    # Been here?
    if node in cache:
        return cache[node]

    if not nodes[node]:
        cache[node] = 2

    elif len(nodes[node]) == 1:
        cache[node] = 1 + count_paths(nodes[node][0])

    elif len(nodes[node]) == 2:
        cache[node] = count_paths(nodes[node][0]) + count_paths(nodes[node][1])

    return cache[node]

print("Part 2:\t", count_paths(start))

