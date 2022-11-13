""" Advent of Code 2018. Day 23: Experimental Emergency Teleportation """

import re

TEST = True
TEST = False

with open("input.txt") as f:
    nanobots = [re.findall(r"-?\d+", line) for line in f.read().splitlines()]

# nanobots = [
#    (0, 0, 0, 4),
#    (1, 0, 0, 1),
#    (4, 0, 0, 3),
#    (0, 2, 0, 1),
#    (0, 5, 0, 3),
#    (0, 0, 3, 1),
#    (1, 1, 1, 1),
#    (1, 1, 2, 1),
#    (1, 3, 1, 1),
# ]
#
if TEST:
    nanobots = [
        (10, 12, 12, 2),
        (12, 14, 12, 2),
        (16, 12, 12, 4),
        (14, 14, 14, 6),
        (50, 50, 50, 200),
        (10, 10, 10, 5),
    ]

class Point:
    def __init__(self, pos):
        self.point = pos
        self.x, self.y, self.z = pos

    def __lt__(self, other):
        return self.point < other.point

    def __eq__(self, other):
        return self.point == other.point

    def __getitem__(self, index):
        return self.point[index]

    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y, self.z - other.z))

    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y, self.z + other.z))

    def __truediv__(self, scalar):
        return Point((self.x // scalar, self.y // scalar, self.z // scalar))

    def manhattan(self):
        return abs(self.x) + abs(self.y) + abs(self.z)



class Bot:
    def __init__(self, pos, r):
        self.pos = Point(pos)
        self.r = r

    def __lt__(self, other):
        return self.r < other.r

    def __eq__(self, other):
        return (self.pos, self.r) == (other.pos, other.r)

    def __hash__(self):
        return hash((self.pos, self.r))

    def __repr__(self):
        return f"Bot({self.pos}, {self.r})"

    def in_bb_range(self, other):
        dist = sum(abs(a - b) for a, b in zip(self.pos, other.pos))
        return dist <= self.r

    def in_range(self, point):
        dist = sum(abs(a - b) for a, b in zip(self.pos, point.point))
        return dist <= self.r


nanobots = [Bot((int(x), int(y), int(z)), int(r)) for x, y, z, r in nanobots]

largest_bot = max(nanobots)
print("Part 1:\t", sum(largest_bot.in_bb_range(bot) for bot in nanobots))

class BBox:
    def __init__(self, lower, upper):
        self.lower = Point(lower)
        self.upper = Point(upper)

    def within_radius_of(self, bot):
        """ If closest edge of box is within bot radius.  """

        dx = (0 if self.lower.x <= bot.pos.x <= self.upper.x else
              abs(self.lower.x - bot.pos.x) if bot.pos.x < self.lower.x else
              abs(self.upper.x - bot.pos.x)
              )
        dy = (0 if self.lower.y <= bot.pos.y <= self.upper.y else
              abs(self.lower.y - bot.pos.y) if bot.pos.y < self.lower.y else
              abs(self.upper.y - bot.pos.y)
              )
        dz = (0 if self.lower.z <= bot.pos.z <= self.upper.z else
              abs(self.lower.z - bot.pos.z) if bot.pos.z < self.lower.z else
              abs(self.upper.z - bot.pos.z)
              )

        return dx + dy + dz <= bot.r

class Octree:
    def __init__(self, nanobots=None, bbox=None):
        self.nanobots = nanobots
        self.bbox = bbox
        self.dims =  self.bbox.upper - self.bbox.lower
        self.is_point = False

    def __lt__(self, other):
        return (len(self.nanobots), self.dims) < (len(other.nanobots), other.dims) 

    def create_points(self):
        lower = self.bbox.lower
        upper = self.bbox.upper

        self.octants = [Point(lower),
            Point((lower.x, lower.y, upper.z)),
            Point((lower.x, upper.y, lower.z)),
            Point((lower.x, upper.y, upper.z)),
            Point((upper.x, lower.y, lower.z)),
            Point((upper.x, lower.y, upper.z)),
            Point((upper.x, upper.y, lower.z)),
            Point(upper)
        ]

    def create_octants(self):
        #mid = self.dims / 2
        center = self.bbox.lower + self.dims / 2

        lower = self.bbox.lower
        upper = self.bbox.upper

        self.octants = [ BBox(lower=lower, upper=center),
             BBox((center.x, lower.y, lower.z), (upper.x, center.y, center.z)),
             BBox((center.x, center.y, lower.z), (upper.x, upper.y, center.z)),
             BBox((lower.x, center.y, lower.z), (center.x, upper.y, center.z)),
             BBox((lower.x, lower.y, center.z), (center.x, center.y, upper.z)),
             BBox((center.x, lower.y, center.z), (upper.x, center.y, upper.z)),
             BBox((center.x, center.y, center.z), (upper.x, upper.y, upper.z)),
             BBox((lower.x, center.y, center.z), (center.x, upper.y, upper.z))
        ]

    def build(self):
        if self.dims.point == (1, 1, 1):
            self.is_point = True
            self.create_points()

            self.octlist = [
                [bot for bot in self.nanobots if bot.in_range(point)]
                for point in self.octants
            ]
        else:
            self.create_octants()

            self.octlist = [
                [bot for bot in self.nanobots if octant.within_radius_of(bot)]
                for octant in self.octants
            ]

from heapq import heappush
from heapq import heappop

import math

def create_bbox(nanobots):
    xmin = nanobots[0].pos[0]
    xmax = nanobots[0].pos[0]
    ymin = nanobots[0].pos[1]
    ymax = nanobots[0].pos[1]
    zmin = nanobots[0].pos[2]
    zmax = nanobots[0].pos[2]

    for bot in nanobots[1:]:
        xmin = min(xmin, bot.pos[0])
        xmax = max(xmax, bot.pos[0])
        ymin = min(ymin, bot.pos[1])
        ymax = max(ymax, bot.pos[1])
        zmin = min(zmin, bot.pos[2])
        zmax = max(zmax, bot.pos[2])

    lower, upper = (Point((xmin, ymin, zmin)), Point((xmax, ymax, zmax)))
    bbox = BBox(lower, upper)

    # Just making sure the cube divisible by 2
    dim = bbox.upper - bbox.lower
    r = math.ceil(max([math.log(d, 2) for d in dim]))
    p = Point([2**r for d in dim])

    bbox.upper = bbox.lower + p

    return bbox

octree = Octree(nanobots, bbox=create_bbox(nanobots))

queue = [(0,0,0,octree)]

while queue:
    *__, octree = heappop(queue)

    # Building the largest child
    octree.build()

    bots, cubes = octree.octlist, octree.octants

    if octree.is_point:
        __, answer = min(
            (-len(bots), pt.manhattan()) for bots, pt in zip(bots, cubes)
        )
        
        print("Part 2: ", answer)

        # Safe to break here, as this is the 1x1x1 cube with the highest number of bots
        break

    # If still not a 1x1x1 cube,
    # we divide the current cube into 8 subcubes 
    # Perhaps all subcubes should be stored, but it worked, so I won't change it
    highest = max(len(b) for b in bots)

    for bot, cube in zip(bots, cubes):
        if len(bot) == highest:
            # We only instantiate the new cube, we don't bother building it yet
            new_tree = Octree(nanobots=bot, bbox=cube)

            # Add the subcubes to priority queue
            heappush(queue, (-highest, new_tree.bbox.lower.manhattan(), new_tree.dims, new_tree)) 
