""" Advent of Code 2017. Day 20: Particle Swarm """
import numpy as np


with open("input.txt") as f:
    particles = f.read().splitlines()
import re

points = np.array(
    [[int(n) for n in re.findall(r"-?\d+", particle)] for particle in particles]
)

counts = 0
prev = 0
while True:
    points[:, 3:6] += points[:, 6:]
    points[:, :3] += points[:, 3:6]

    closest = np.abs(points[:, :3]).sum(axis=1).argmin()
    counts = 1 if closest != prev else counts + 1
    prev = closest
    if counts > 500:
        # Assuming this is enough
        break
print("Part 1:\t", closest)

points = np.array(
    [[int(n) for n in re.findall(r"-?\d+", particle)] for particle in particles]
)

counter = 0
while True:
    points[:, 3:6] += points[:, 6:]
    points[:, :3] += points[:, 3:6]

    __, idc, counts = np.unique(
        points[:, :3], axis=0, return_index=True, return_counts=True
    )
    idc = idc[counts == 1]

    if len(idc) < len(points):
        points = points[idc]
        counter = 0
    else:
        counter += 1

    if counter > 100:
        break


print("Part 2:\t", len(points))
