""" Advent of Code 2023. Day 23: A Long Walk"""

with open("input.txt") as f:
    trails = f.read().splitlines()

paths = set()
slopes = dict()

for y, row in enumerate(trails):
    for x, cell in enumerate(row):
        if "." in cell:
            paths.add((x, y))
        elif cell in "<>^v":
            slopes[(x, y)] = cell


def bfs(startnode, goal):
    queue = [startnode]

    while queue:
        n = queue.pop(0)

        for direction, dx, dy in [("v", 0, 1), ("^", 0, -1), (">", 1, 0), ("<", -1, 0)]:
            x, y = n.x + dx, n.y + dy

            if (x, y) == n.prev:
                continue

            if (x, y) in paths or ((x, y) in slopes and direction == slopes[(x, y)]):
                new_node = Node(n.cost + 1, x, y, (n.x, n.y))
                queue.append(new_node)
    return n.cost


from collections import namedtuple

Node = namedtuple("Node", "cost x y prev")
node = Node(0, 1, 0, (0, 0))
goal = (len(trails[0]) - 2, len(trails) - 1)
print("Part 1:\t", bfs(node, goal=goal))

# Let's create a condensed graph in stead, where the crossroads are nodes
# with edges with length equalling number of steps

from collections import defaultdict


def dfs(startnode, goal):
    queue = [startnode]
    seen = dict()

    dists = defaultdict(dict)

    while queue:
        n = queue.pop()

        if (n.x, n.y) == goal:
            dists[n.parent][(n.x, n.y)] = n.cost
            # dists[(n.x, n.y)][n.parent] = n.cost
            seen[(n.x, n.y)] = n.parent
            continue

        if (n.x, n.y) in seen:
            # Let's join the links
            if (n.x, n.y) in dists:
                dists[n.parent][(n.x, n.y)] = n.cost
                dists[(n.x, n.y)][n.parent] = n.cost

            continue

        seen[(n.x, n.y)] = n.parent

        branches = []
        for direction, dx, dy in [("v", 0, 1), ("^", 0, -1), (">", 1, 0), ("<", -1, 0)]:
            x, y = n.x + dx, n.y + dy

            if (x, y) == n.prev:
                continue

            if (x, y) in paths | slopes.keys():
                new_cost = n.cost + 1
                new_node = Node(new_cost, x, y, (n.x, n.y), n.parent)
                branches.append(new_node)

        if len(branches) > 1:
            # At a crossroads
            dists[n.parent][(n.x, n.y)] = n.cost
            dists[(n.x, n.y)][n.parent] = n.cost

            branches = [
                Node(1, branch.x, branch.y, (n.x, n.y), (n.x, n.y))
                for branch in branches
            ]

        queue.extend(branches)
    return dists


Node = namedtuple("Node", "cost x y prev parent")
node = Node(0, 1, 0, (0, 0), (0, 0))
goal = (len(trails[0]) - 2, len(trails) - 1)

# First, condense the maze to a graph
graph = dfs(node, goal)


costs = []


# Then, traverse the graph, exploring all possible routes
def traverse(node, cost, visited):
    if node == goal:
        costs.append(cost)
        return

    for child in graph[node]:
        if child in visited:
            # Avoid endless cycles
            continue

        traverse(child, cost + graph[node][child], visited | {node})


visited = set()
traverse((0, 0), 0, visited)
print("Part 2:\t", max(costs))
