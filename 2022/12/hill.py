""" Advent of Code 2022. Day 12: Hill Climbing Algorithm """

with open("input.txt") as f:
    diagram = f.read().splitlines()

candidates = []
for i, line in enumerate(diagram):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
            candidates.append((i, j))
        elif c == "a":
            candidates.append((i, j))
        elif c == "E":
            goal = (i, j)

def expand(x, y):
    queue = []
    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        x1, y1 = x+dx, y+dy

        if 0<=x1<len(diagram) and 0<=y1<len(diagram[0]):
            if (x1, y1) == goal and diagram[x][y] in "yz":
                queue.append((x1,y1))
            elif (x1, y1) == goal and diagram[x][y] != "z":
                continue
            elif ord(diagram[x1][y1]) <= ord(diagram[x][y]) + 1:
                # Can move here
                queue.append((x1,y1))
            elif diagram[x][y] == "S" and diagram[x1][y1] == "a":
                # Can move here
                queue.append((x1, y1))
    return queue

def heuristic(x, y, goal):
    return abs(goal[0]-x) + abs(goal[1]-y)

from heapq import heappush
from heapq import heappop

def astar(starts):
    queue = []
    cost = dict()

    for start in starts:
        heappush(queue, (0, start))
        cost[start] = 0

    while queue:
        __, pos = heappop(queue)

        if pos == goal:
            return cost[pos]
        
        for n in expand(*pos):
            if n not in cost or cost[pos] + 1 < cost[n]:
                cost[n] = cost[pos]+1
                priority = cost[pos]+1 + heuristic(*n, goal)
                heappush(queue, (priority, n))

print("Part 1:\t", astar([start]))
print("Part 2:\t", astar(candidates))
