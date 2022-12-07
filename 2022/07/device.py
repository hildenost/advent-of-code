""" Advent of Code 2022. Day 7: No Space Left On Device """

with open("input.txt") as f:
    cmds = f.read().splitlines()

sizes = {}
cwds = []
for line in cmds:
    a, b, *c = line.split()

    if b == "cd":
        if c[0] == "..":
            cwds.pop()
        else:
            cwds.append(*c)
            sizes[tuple(cwds)] = 0

    if a.isdigit():
        for l in range(len(cwds)):
            sizes[tuple(cwds[:l+1])] += int(a)

part1 = sum(s for s in sizes.values() if s <= 100000)
print("Part 1:\t", part1)

ALL = 70000000
NEEDED = 30000000
size_outer = sizes[("/",)] 
treshold = NEEDED - (ALL - size_outer)
part2 = min(s for s in sizes.values() if s >= treshold)
print("Part 2:\t", part2)
