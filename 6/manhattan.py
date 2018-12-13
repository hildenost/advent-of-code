""" Day 6: Chronal Coordinates """
import sys
from operator import itemgetter


def manhattan(p, q):
    return sum(abs(xp - xq) for xp, xq in zip(p,q))

coordinates = [tuple(int(x) for x in coordinate.strip().split(", "))
               for coordinate in sys.stdin.readlines()]

area = [0]*len(coordinates)

# Strategy: If infinite area, the area will decrease depending
# on the boundary coordinates.
# Will run first over a minimum area, covering just each coordinate.
# Then expand total area by 1 in each dimension, and run over those
# as well.
# Those areas that change, are infinite.

def assign_area(x, y, coordinates, area):
    distances = [manhattan((x,y), c) for c in coordinates]
    idx, distance = min(enumerate(distances), key=itemgetter(1))
    # Checking for duplicates
    if not distance in distances[:idx]+distances[idx+1:]:
        area[idx] += 1

y_max = max(c[1] for c in coordinates) + 1
x_max = max(c[0] for c in coordinates) + 1
for x in range(x_max):
    for y in range(y_max):
        assign_area(x, y, coordinates, area)

extraarea = [a for a in area]
for x in [-1, x_max+2]:
    for y in range(y_max):
        assign_area(x, y, coordinates, extraarea)

for y in [-1, y_max+2]:
    for x in range(x_max):
        assign_area(x, y, coordinates, extraarea)

print(max(a for a, b in zip(area, extraarea) if a == b))

## Part 2
threshold = 10000
print(sum(1
          for x in range(x_max)
          for y in range(y_max)
          if sum(manhattan((x,y), c) for c in coordinates) < threshold))
