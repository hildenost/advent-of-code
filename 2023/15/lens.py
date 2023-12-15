""" Advent of Code 2023. Day 15: Lens Library """

with open("input.txt") as f:
    steps = f.read().split(",")


def hash(string):
    curr = 0
    for letter in string:
        curr += ord(letter)
        curr *= 17
        curr %= 256
    return curr


print("Part 1:\t", sum(hash(step) for step in steps))

from collections import defaultdict

hashmap = defaultdict(dict)

for step in steps:
    opchar = step[-1]

    if opchar == "-":
        lens = step[:-1]
        h = hash(lens)
        if lens in hashmap[h]:
            del hashmap[h][lens]
    else:
        focal_length = int(opchar)
        lens = step[:-2]
        h = hash(lens)

        hashmap[h][lens] = focal_length

boxsum = sum(
    sum((box + 1) * (i + 1) * v for i, v in enumerate(slots.values()))
    for box, slots in hashmap.items()
)
print("Part 2:\t", boxsum)
