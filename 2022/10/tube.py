""" Advent of Code. Day 10: Cathode-Ray Tube """
from itertools import count

with open("input.txt") as f:
    program = f.read().splitlines()[::-1]

intervals = {k: 0 for k in (20, 60, 100, 140, 180, 220)}
X = 1
signal_strength = 0
active = ("", 0, 0)
for c in count():
    if c in intervals:
        signal_strength += c * X
    cmd, counter, n = active

    if counter > 0:
        active = (cmd, counter-1, n)
        continue

    # Add to X
    X += n
    # Exit if program done
    if not program:
        break
    # Do next instruction
    match program.pop().split():
        case ["noop"]:
            active = ("noop", 0, 0)
        case ["addx", number]:
            active = ("addx", 1, int(number))
            
print("Part 1:\t", signal_strength)
with open("input.txt") as f:
    program = f.read().splitlines()[::-1]


intervals = {k: 0 for k in (20, 60, 100, 140, 180, 220)}
crt = []
X = 1
active = ("", 0, 0)
for c in count():
    cmd, counter, n = active
    if counter == 0:
        # Add to X
        X += n

    crt.append("#" if c%40 in range(X-1,X+2) else ".")

    if counter > 0:
        active = (cmd, counter-1, n)
        continue

    # Exit if program done
    if not program:
        break
    # Do next instruction
    match program.pop().split():
        case ["noop"]:
            active = ("noop", 0, 0)
        case ["addx", number]:
            active = ("addx", 1, int(number))

for i in range(0, 241,40):
    print("".join(crt[i:i+40]))
