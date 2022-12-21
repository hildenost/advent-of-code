""" Advent of Code 2022. Day 18: Boiling Boulders """

sample = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".splitlines()

with open("input.txt") as f:
    sample = f.read().splitlines()

cubes = {tuple(int(n) for n in cube.split(",")) for cube in sample}

def neighbours(x, y, z):
    return [
        (x+1, y, z),
        (x-1, y, z),
        (x, y+1, z),
        (x, y-1, z),
        (x, y, z+1),
        (x, y, z-1)
    ]

# Adding the number of free sides of each cube
surface = sum(
    neighbour not in cubes
    for cube in cubes
    for neighbour in neighbours(*cube)
)

print("Part 1:\t", surface)

# Finding the enclosing region of the lava droplet
xmax = max(cubes, key=lambda x:x[0])[0]+1
ymax = max(cubes, key=lambda x:x[1])[1]+1
zmax = max(cubes, key=lambda x:x[2])[2]+1
xmin = min(cubes, key=lambda x:x[0])[0]-1
ymin = min(cubes, key=lambda x:x[1])[1]-1
zmin = min(cubes, key=lambda x:x[2])[2]-1

# Start from the outskirts of the enclosing regions
# and collect air cubes
queue = [(xmax, ymax, zmax)]
air = set()
while queue:
    cube = queue.pop(0)

    if cube not in cubes:
        air.add(cube)

    queue.extend(
        [(x, y, z)
         for (x, y, z) in neighbours(*cube)
         if (x, y, z) not in air | cubes
         and (x, y, z) not in queue
         and xmin-1 <= x <= xmax+1
         and ymin-1 <= y <= ymax+1
         and zmin-1 <= z <= zmax+1])

air_surfaces = sum(
    neighbour in cubes
    for cube in air
    for neighbour in neighbours(*cube)
)
print("Part 2:\t", air_surfaces)

exit()
# Visualisation
import matplotlib.pyplot as plt
import numpy as np
A = np.zeros((xmax+1, ymax+1, zmax+1), dtype=bool)
for x, y, z in cubes:
    A[x, y, z] = True

print(A)

ax = plt.figure().add_subplot(projection="3d")
ax.voxels(A, alpha=0.3)
ax.set_aspect("equal")

plt.savefig("test.png")
