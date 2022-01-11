""" Advent of Code 2016. Day 24: Air Duct Spelunking """
import re

grid = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########
""".splitlines()

with open("input.txt") as f:
    grid = f.read().splitlines()


locations = {
    match[0]: (match.start(), i)
    for i, row in enumerate(grid)
    for match in re.finditer(r"\d", row)
}
for loc, (j, i) in locations.items():
    assert grid[i][j] == loc


class Node:
    def __init__(self, pos, goal, steps=0, came_from=None):
        self.pos = pos
        self.goal = goal
        # self.visited = set("0") if visited is None else visited

        self.h = self.heuristic()
        self.g = steps
        self.score = self.g + self.h

        self.came_from = came_from

    def heuristic(self):
        return sum(abs(self.pos[i] - self.goal[i]) for i in range(2))

    def __lt__(self, other):
        if self.score == other.score:
            return self.g > other.g
        return self.score < other.score

    def __eq__(self, other):
        return (self.pos) == (other.pos)

    def __hash__(self):
        return hash(self.pos)

    def __repr__(self):
        return f"Node({self.pos}, steps={self.g}, h={self.h}, score={self.score})"


def expand(node):
    x, y = node.pos

    queue = []
    # Can go up, down, left, right
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if node.came_from is not None and (x + dx, y + dy) == node.came_from.pos:
            # Cannot turn
            continue

        if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]):
            square = grid[y + dy][x + dx]
            if square == "." or square in locations:
                queue.append(
                    Node((x + dx, y + dy), node.goal, node.g + 1, came_from=node)
                )
    return queue


from heapq import heappush
from heapq import heappop


def astar(startnode):
    open_list = [startnode]
    closed_list = set()

    while open_list:
        n = heappop(open_list)

        if n in closed_list:
            continue

        closed_list.add(n)

        if n.pos == n.goal:
            return n.g

        children = expand(n)

        for c in children:
            if c in closed_list:
                continue
            heappush(open_list, c)

    print()
    print("Explored ", len(closed_list), " nodes")
    return "NO SOLUTION"


from itertools import combinations
from itertools import permutations
from collections import defaultdict

# Do astar on all possible goals from start
# Then do that on all other nodes to get all pairs shortest path
graph = defaultdict(dict)
for start, goal in combinations(locations, 2):
    startnode = Node(locations[start], goal=locations[goal])
    weight = astar(startnode)

    graph[start][goal] = weight
    graph[goal][start] = weight


min_route = 100000000
for route in permutations(locations.keys() - {"0"}):
    route = ["0"] + list(route)
    cost = sum(graph[start][goal] for start, goal in zip(route, route[1:]))
    min_route = min(min_route, cost)
print("Part 1:\t", min_route)

min_route = 100000000
for route in permutations(locations.keys() - {"0"}):
    route = ["0"] + list(route) + ["0"]
    cost = sum(graph[start][goal] for start, goal in zip(route, route[1:]))
    min_route = min(min_route, cost)
print("Part 2:\t", min_route)
