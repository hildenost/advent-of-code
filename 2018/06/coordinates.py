""" Advent of Code 2018. Day 6: Chronal Coordinates """

with open("input.txt") as f:
    coords = [
        tuple(int(c) for c in line.split(","))
        for line in f.read().splitlines()
    ]

xs, ys = zip(*coords)

# The bounding box
# Coords at the bounding box have infinite areas
xmin = min(xs)
xmax = max(xs)
ymin = min(ys)
ymax = max(ys)

s = max(ymax-ymin, xmax - xmin)

def manhattan(p, q):
    return sum(abs(xp - xq) for xp, xq in zip(p,q))

from operator import itemgetter
def assign_area(x, y, coordinates, area):
    distances = [manhattan((x,y), c) for c in coordinates]
    idx, distance = min(enumerate(distances), key=itemgetter(1))

    x, y = coords[idx]
    if xmin < x < xmax and ymin < y < ymax:
        # Checking for duplicates
        if not distance in distances[:idx]+distances[idx+1:]:
            area[idx] += 1

area = [0]*len(coords)
for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        assign_area(x, y, coords, area)
print("Part 1:\t", max(area))
threshold = 10000
print("Part 2:\t", sum(sum(manhattan((x,y), c) for c in coords) < threshold
                       for x in range(xmin, xmax + 1)
                       for y in range(ymin, ymax + 1)))
