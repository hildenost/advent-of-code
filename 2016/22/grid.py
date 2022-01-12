""" Advent of Code 2016. Day 22: Grid Computing """
import re

df = """/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%
""".splitlines()

with open("input.txt") as f:
    __, __, *df = f.read().splitlines()

pattern = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)\s+\w+\s+(\d+)T\s+(\d+)T")

# Initialize grid
grid = {}
space = {}
for line in df:
    x, y, used, avail = [int(g) for g in re.search(pattern, line).groups()]
    grid[(x, y)] = used
    space[(x, y)] = avail
    if used == 0:
        empty = (x, y)


SIZE, __ = max(grid.keys())

all_nodes = [(x, y) for x in range(SIZE + 1) for y in range(SIZE + 1)]
# print(all_nodes)

viable_pairs = sum(
    grid[A] <= space[B] for A in all_nodes for B in all_nodes if grid[A] > 0 and A != B
)

print("Part 1:\t", viable_pairs)


def draw(grid, threshold=9999, current=None, visited=None):
    size, __ = max(grid.keys())
    for y in range(size + 1):
        row = ""
        for x in range(size + 1):
            if grid[(x, y)] == 0:
                row += "  O  "
            elif (x, y) == (0, 0):
                row += " (.) "
            elif (x, y) == (size, 0):
                row += "  G  "
            elif grid[(x, y)] > threshold:
                row += "  #  "
            elif current is not None and (x, y) == current:
                row += "  *  "
            elif visited is not None and (x, y) in visited:
                row += f"  {visited[(x, y)]:2d} "
            else:
                row += "  .  "
        print(row)


# First, let's visually inspect the grid

# After taking a glance at the input data,
# it seems some nodes are ridiculously larger
# than the rest. Testing with a threshold of 100.
draw(grid, threshold=100)

# I initially solved the problem by manually
# counting the steps

# The problem is two-part:
# 1. Move the empty space next to the goal data
# 2. Move the goal data along the top row

import math

# First part will be solved using A*
class Node:
    def __init__(self, pos, goal, cost=0):
        self.pos = pos
        self.goal = goal
        self.g = cost
        self.h = self.heuristic()
        self.score = self.g + self.h

    def heuristic(self):
        return sum(abs(a - b) for a, b in zip(self.pos, self.goal))

    def __lt__(self, other):
        if self.score == other.score:
            return self.g > other.g
        return self.score < other.score

    def __eq__(self, other):
        return (self.pos) == (other.pos)

    def __hash__(self):
        return hash(self.pos)

    def __repr__(self):
        return f"Node({self.pos}, score={self.score}, h={self.h})"


THRESHOLD = 100


def expand(node):
    x, y = node.pos
    queue = []
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, -1)]:
        if grid.get((x + dx, y + dy), THRESHOLD) < THRESHOLD:
            queue.append(Node((x + dx, y + dy), node.goal, node.g + 1))
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


startnode = Node(empty, (SIZE - 1, 0))

# First number of steps:
to_goal = astar(startnode)
# For the second part, it takes 5 steps to move the
# goal data one step to the left
# Note that the final nudge only requires 1 step
to_output = 5 * (SIZE - 1) + 1
print("Part 2:\t", to_goal + to_output)
