""" Advent of Code 2022. Day 24: Blizzard Basin """

with open("input.txt") as f:
    sample = f.read().splitlines()

xmax = len(sample[0]) - 2
ymax = len(sample) - 2

class Blizzard:
    def __init__(self, pos, face):
        self.x, self.y = pos
        self.face = face

    def move(self):
        if self.face == ">":
            self.x += 1
            self.x %= xmax
        elif self.face == "^":
            self.y -= 1
            self.y %= ymax
        elif self.face == "<":
            self.x -= 1
            self.x %= xmax
        elif self.face == "v":
            self.y += 1
            self.y %= ymax

    def __repr__(self):
        return f"({self.x}, {self.y})"

blizzards = [
    Blizzard((j, i), col)
    #(j, i, col)
    for i, row in enumerate(sample[1:])
    for j, col in enumerate(row[1:])
    if col in "><v^"
]
#blizzards = {(j, i): col
#    for i, row in enumerate(sample[1:])
#    for j, col in enumerate(row[1:])
#    if col in "><v^"
#    }

walls = {(-1, y) for y in range(-1, len(sample))}
walls.update({(xmax, y) for y in range(-1, len(sample))})
walls.update({(x, -1) for x in range(1, xmax)})
walls.update({(x, ymax) for x in range(0, xmax-1)})
walls.add((0, -2))
walls.add((xmax-1, ymax+1))

def expand(x, y, busy):
    return [
        (x+dx, y+dy)
        for dx, dy in [(0, 0), (0, -1), (0, 1), (1, 0), (-1, 0)]
        if (x+dx, y+dy) not in busy | walls
    ]

from copy import deepcopy
from heapq import heappush
from heapq import heappop


def heuristic(x, y, goal):
    return abs(goal[0]-x) + abs(goal[1]-y)

blizzes = {}
blizzes[0] = blizzards

def astar(start, goal, time=0):
    queue = []
    heappush(queue, (0, -time, start))
    visited = {(start, time)}

    while queue:
        __, t, pos = heappop(queue)

        t = -t

        if pos == goal:
            return t

        # Move blizzards
        if not (t+1) in blizzes:
            blizzes[t+1] = [deepcopy(b) for b in blizzes[t]]
            for b in blizzes[t+1]:
                b.move()

        busy = {(b.x, b.y) for b in blizzes[t+1]}
        
        for neighbour in expand(*pos, busy):
            if (neighbour, t+1) not in visited:
                visited.add((neighbour, t+1))
                priority = t+1 + heuristic(*neighbour, goal)
                heappush(queue, (priority, -(t+1), neighbour))

curr = (0, -1)
goal = (xmax-1, ymax)

first_mins = astar(curr, goal)
print("Part 1:\t", first_mins)
second_mins = astar(goal, goal=curr, time=first_mins)
print(second_mins)
print("Part 2:\t", astar(curr, goal, time=second_mins)) 

