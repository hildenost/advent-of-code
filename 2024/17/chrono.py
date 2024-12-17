""" Advent of Code 2024. Day 17: Chronospatial Computer """

from computer import run


with open("input.txt") as f:
    program = f.read().split("\n\n")

import re

A, B, C = [int(n) for n in re.findall(r"\d+", program[0])]
program = [int(n) for n in re.findall(r"\d", program[1])]

print("Part 1:\t", ",".join(run(program, A=A, B=B, C=C)))

# Let's be smart and fix the problem from behind
# The number should be 3 * len(program) in binary
# The outputted program number is based on the last 3 bits
# Let's decide the last (or actually first) 3 bits of A
# And then work our way back (or forward)


options = []

queue = [""]
while queue:
    # Can make this more efficient by following the
    # minimum trail
    n = queue.pop()

    # digit placement
    i = len(n) // 3

    if i >= len(program):
        # We have a solution, store it for later
        options.append(int(n, 2))

    # Select the last i program commands
    prog = program[::-1][: i + 1]

    # The next digit will be in range [0, 7]
    for a in range(8):
        test = int(n + f"{a:03b}", 2)
        output = run(program, A=test, B=0, C=0)

        if output == [str(p) for p in prog[::-1]]:
            # We found a candidate for the ith digit
            queue.append(n + f"{a:03b}")

print("Part 2:\t", min(options))
