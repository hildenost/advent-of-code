""" Advent of Code 2023. Day 03: Gear Ratios """
import re

with open("input.txt") as f:
    schematic = f.readlines()

width = len(schematic[0])

schematic = "".join(schematic)

poses = {p.start() for p in re.finditer(r"(\D)", schematic) if p[1] not in [".", "\n"]}


def has_part(start, end):
    for i in range(start, end):
        for di in (-1, 1, -width, width, -width - 1, -width + 1, width - 1, width + 1):
            if i + di in poses:
                return True
    return False


answer = sum(
    int(m[1]) for m in re.finditer(r"(\d+)", schematic) if has_part(m.start(), m.end())
)
print("Part 1:\t", answer)

poses = {p.start() for p in re.finditer(r"\d", schematic)}
gears = {p.start() for p in re.finditer(r"\*", schematic)}

parts = dict()
for m in re.finditer(r"(\d+)", schematic):
    for i in range(m.start(), m.end()):
        parts[i] = int(m[1])


def count_parts(i):
    neighbours = set()
    for di in (-1, 1, -width, width, -width - 1, -width + 1, width - 1, width + 1):
        if i + di in parts:
            neighbours.add(parts[i + di])
    if len(neighbours) == 2:
        a, b = neighbours
        return a * b
    return 0


answer = sum(count_parts(gear) for gear in gears)
print("Part 2:\t", answer)
