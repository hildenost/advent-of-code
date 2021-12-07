""" Advent of Code 2016. Day 8: Two-Factor Authentication """

import re

width, height = 50, 6
#width, height = 7, 3

screen = [
    ["." for __ in range(width)]
    for __ in range(height)
]


def draw(screen):
    for row in screen:
        print("".join(r if r == "#" else " " for r in row))

with open("input.txt") as f:
    ops = f.read().splitlines()

for op in ops:
    if op.startswith("rect"):
        A, B = re.findall(r"(\d+)", op)
        for i in range(int(B)):
            for j in range(int(A)):
                screen[i][j] = "#"
    elif op.startswith("rotate column"):
        A, B = re.findall(r"(\d+)", op)
        column = [s[int(A)] for s in screen]
        for i in range(len(screen)):
            idx = (i + int(B)) % len(screen)
            screen[idx][int(A)] = column[i]
    elif op.startswith("rotate row"):
        A, B = re.findall(r"(\d+)", op)
        row = screen[int(A)].copy()
        for i in range(len(screen[0])):
            idx = (i + int(B)) % len(screen[0])
            screen[int(A)][idx] = row[i]

        
print("Part 1:\t", sum(s == "#" for row in screen for s in row))

print("Part 2:\t")
draw(screen)



