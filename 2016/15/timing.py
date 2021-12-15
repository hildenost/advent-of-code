""" Advent of Code 2016. Day 15: Timing is Everything """

raw_disks = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".splitlines()

import re

disks = []
pattern = re.compile(r"(\d+)")
for disk in raw_disks:
    __, pos, __, p0 = re.findall(pattern, disk)
    disks.append((int(pos), int(p0)))


def arrange(disks):
    time = 0
    while True:
        if all([(time + i + 1 + p) % pos == 0 for i, (pos, p) in enumerate(disks)]):
            return time

        time += 1


print("Part 1:\t", arrange(disks))

disks.append((11, 0))
print("Part 2:\t", arrange(disks))
