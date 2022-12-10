""" Advent of Code. Day 10: Cathode-Ray Tube """
from itertools import count

with open("input.txt") as f:
    program = f.read().splitlines()[::-1]

X = 1
counter = 0
n = 0
# Part 1
intervals = {20, 60, 100, 140, 180, 220}
signal_strength = 0
# Part 2
crt = []

for c in count():
    if c in intervals:
        signal_strength += c * X

    if counter == 0:
        # Add to X
        X += n

    crt.append("█" if c%40 in range(X-1,X+2) else " ")

    if counter > 0:
        counter -= 1
        continue

    # Exit if program done
    if not program:
        break

    # Do next instruction
    match program.pop().split():
        case ["noop"]:
            counter = 0
            n = 0
        case ["addx", number]:
            counter = 1
            n = int(number)
            
print("Part 1:\t", signal_strength)
print("Part 2:")
for i in range(0, 240,40):
    print("".join(crt[i:i+40]))
