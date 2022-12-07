""" Advent of Code 2022. Day 7: No Space Left On Device """

sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

sample = sample.splitlines()

with open("input.txt") as f:
    sample = f.read().splitlines()

sizes = {}
cwds = []

for i in range(len(sample)):
    a, b, *c = sample[i].split()

    if b == "cd":
        cwd = c[0]
        if cwd == "..":
            cwds.pop()
        else:
            cwds.append(cwd)
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
