""" Advent of Code 2023. Day 17: Clumsy Crucible """
from collections import namedtuple
from heapq import heappush
from heapq import heappop

with open("input.txt") as f:
    heatmap = f.read().splitlines()

heatmap = [[int(n) for n in row] for row in heatmap]
width, height = len(heatmap[0]), len(heatmap)


def neighbours(x, y, direction):
    if direction == ">":
        return [(x + 1, y, direction), (x, y + 1, "v"), (x, y - 1, "^")]
    if direction == "<":
        return [(x - 1, y, direction), (x, y + 1, "v"), (x, y - 1, "^")]
    if direction == "^":
        return [(x + 1, y, ">"), (x - 1, y, "<"), (x, y - 1, "^")]
    if direction == "v":
        return [(x + 1, y, ">"), (x - 1, y, "<"), (x, y + 1, "v")]


def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# node = (priority, cost, x, y, direction, consecutive dirs)


def astar(startnodes, goal, max_consecutive=3, min_consecutive=1):
    queue = [*startnodes]

    seen = set()

    while queue:
        n = heappop(queue)

        if (n.x, n.y, n.direction, n.consecutive) in seen:
            # We've been here, so this path is not the best solution
            continue

        seen.add((n.x, n.y, n.direction, n.consecutive))

        if goal == (n.x, n.y) and n.consecutive >= min_consecutive:
            return n.cost

        for x, y, direction in neighbours(n.x, n.y, n.direction):
            if not (0 <= x < width and 0 <= y < height):
                # Out of bounds
                continue

            if n.consecutive > max_consecutive:
                # Illegal path
                continue

            if direction == n.direction:
                # Same direction
                consecutive = n.consecutive + 1
            else:
                # Different direction
                # Cannot turn if consecutive is less than the demand
                if n.consecutive < min_consecutive:
                    continue
                consecutive = 1

            if (x, y, direction, consecutive) not in seen:
                new_cost = n.cost + heatmap[y][x]
                h = heuristic(x, y, *goal)
                new_node = Node(new_cost + h, new_cost, x, y, direction, consecutive)
                heappush(queue, new_node)


goal = (width - 1, height - 1)
h = heuristic(0, 0, *goal)

Node = namedtuple("Node", "priority cost x y direction consecutive")
node = Node(h, 0, 0, 0, ">", 1)
node_2 = Node(h, 0, 0, 0, "v", 1)
print("Part 1:\t", astar([node, node_2], goal=goal))
print(
    "Part 2:\t", astar([node, node_2], goal=goal, max_consecutive=10, min_consecutive=4)
)
