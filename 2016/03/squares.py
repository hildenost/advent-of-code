""" Advent of Code 2016. Day 3: Squares With Three Sides """

with open("input.txt") as f:
  triangles = [
    [int(l) for l in line.split()]
    for line in f.read().splitlines()
    ]


print("Part 1:\t", sum(a + b > c for a, b, c in (sorted(t) for t in triangles)))

counter = 0
for i in range(0, len(triangles), 3):
  for k in range(3):
    a, b, c = sorted([triangles[i+j][k] for j in range(3)])
    counter += a + b > c

print("Part 2:\t", counter)
