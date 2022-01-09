""" Advent of Code 2021. Day 22: Reactor Reboot """
import re

with open("input.txt") as f:
    reboot = f.read().splitlines()

pattern = re.compile(r"(-?\d+)")

cuboids = [tuple(int(n) for n in re.findall(pattern, step))
    for step in reboot]
cmds = [step.split()[0] for step in reboot]

def is_overlap(A, B):
    # A/B = xmin, xmax, ymin, ymax, zmin, zmax
    is_NOT_x_overlap = A[1] < B[0] or A[0] > B[1]
    is_NOT_y_overlap = A[3] < B[2] or A[2] > B[3]
    is_NOT_z_overlap = A[5] < B[4] or A[4] > B[5]
    return not (
        is_NOT_x_overlap or
        is_NOT_y_overlap or
        is_NOT_z_overlap)

def overlap_volume(*cubes):
    xmin = max(c[0] for c in cubes)
    xmax = min(c[1] for c in cubes)
    ymin = max(c[2] for c in cubes)
    ymax = min(c[3] for c in cubes)
    zmin = max(c[4] for c in cubes)
    zmax = min(c[5] for c in cubes)
    return (xmin, xmax, ymin, ymax, zmin, zmax)

def compute_volume(a):
    w = a[1] + 1 - a[0]
    h = a[3] + 1 - a[2]
    b = a[5] + 1 - a[4]
    return w*h*b

def find_cuboid_volume(cuboid, rest):
    # First we compare with the remaining cuboids in list
    overlaps = [overlap_volume(cuboid, other_cuboid)
                for other_cuboid in rest
                if is_overlap(cuboid, other_cuboid)]

    # Inclusion-exclusion principle: subtracting the overlapping volumes
    # We don't need to do anything special with the off cuboids
    return (compute_volume(cuboid) -
            sum(find_cuboid_volume(cube, overlaps[i+1:])
                for i, cube in enumerate(overlaps))
    )

def solve(cmds, cuboids, limit=None):
    if limit is not None:
        # Must filter out cuboids larger than limit
        cuboids = [cuboid for cuboid in cuboids
                   if all(abs(c) <= limit for c in cuboid)]

    return sum(find_cuboid_volume(cuboid, cuboids[i+1:])
          for i, (cmd, cuboid) in enumerate(zip(cmds, cuboids))
          if cmd == "on")

print("Part 1:\t", solve(cmds, cuboids, limit=50))
print("Part 2:\t", solve(cmds, cuboids))
