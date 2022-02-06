""" Advent of Code 2018. Day 22: Mode Maze """

with open("input.txt") as f:
    depth, target = f.read().splitlines()
    depth = int(depth.split(":")[1])
    X, Y = tuple(int(n) for n in target.split(":")[1].split(","))

def initialize_region(X, Y, depth):
    erosion = dict()
    erosion[(0, 0)] = depth
    erosion.update({(x, 0): (16807*x + depth) % 20183 for x in range(X + 1)})
    erosion.update({(0, y): (48271*y + depth) % 20183 for y in range(Y + 1)})

    for x in range(1, X+1):
        for y in range(1, Y+1):
            erosion[(x, y)] = compute_erosion(x, y, erosion) 
    erosion[(X, Y)] = depth
    return erosion

def expand_erosion(x, y, erosion):
    if x == 0:
        erosion[(0, y)] = (48271*y + depth) % 20183
        return
    if y == 0:
        erosion[(x, 0)] = (16807*x + depth) % 20183
        return

    maxx = [a for a, b in erosion if b == y]
    maxy = [b for a, b in erosion if a == x]

    if not maxx:
        erosion[(0, y)] = (48271*y + depth) % 20183
        maxx = [0]

    if not maxy:
        erosion[(x, 0)] = (16807*x + depth) % 20183
        maxy = [0]

    for a in range(max(maxx) + 1, x+1):
        for b in range(max(maxy) + 1, y+1):
            erosion[(a, b)] = compute_erosion(a, b, erosion) 
    


def compute_erosion(x, y, erosion):
    return (erosion[(x-1, y)]*erosion[(x, y-1)] + depth) % 20183

erosion = initialize_region(X, Y, depth)

types = {pos: value % 3 for pos, value in erosion.items()}

print("Part 1:\t", sum(types.values()))


####
NEITHER = 0
GEAR = 1
TORCH = 2

ROCKY = 0
WET = 1
NARROW = 2

rules = {
    ROCKY: {GEAR, TORCH},
    WET: {GEAR, NEITHER},
    NARROW: {TORCH, NEITHER},
}

def expand(node):
    x, y = node.pos

    children = []
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        if x+dx < 0 or y+dy < 0:
            continue
        # Within bounds
        # What type of region have we here?
        region = types.get((x+dx, y+dy))
        if region is None:
            expand_erosion(x+dx, y+dy, erosion)
            types[(x+dx, y+dy)] = erosion[(x+dx, y+dy)] % 3
            region = types[(x+dx, y+dy)]

        for tool in rules[region] & rules[node.region]:
            if (x+dx, y+dy) == (X, Y):
                if tool != TORCH:
                    continue

            cost = 1 if tool == node.tool else 8
            children.append(
                Node(pos=(x+dx, y+dy), tool=tool, region=region, cost=node.g + cost))

    return children


class Node:
    def __init__(self, pos=(0, 0), tool=TORCH, region=ROCKY, cost=0):
        self.pos = pos 
        self.tool = tool
        self.region = region

        self.g = cost
        self.h = self.heuristic()
        self.score = self.g + self.h

    def heuristic(self):
        """ Try Manhattan first """
        return sum(abs(a-b) for a, b in zip(self.pos, (X, Y))) + (0 if self.tool == TORCH else 7)

    def __hash__(self):
        return hash((self.pos, self.tool))

    def __eq__(self, other):
        return (self.pos, self.tool) == (other.pos, other.tool)

    def __lt__(self, other):
        if self.score == other.score:
            return self.g > other.g
        return self.score < other.score


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

        if n.h == 0:
            print("Explored ", len(closed_list), " nodes")
            return n.g
       
        children = expand(n)

        for c in children:
            if c in closed_list:
                continue
            heappush(open_list, c)
    print("Explored ", len(closed_list), " nodes")
        
print("Part 2:\t", astar(Node()))
