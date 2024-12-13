""" Advent of Code 2024. Day 13: Claw Contraption """

rawlist = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".split(
    "\n\n"
)

with open("input.txt") as f:
    rawlist = f.read().split("\n\n")

import re


def parse_machine(machine, offset=0):
    m = machine.splitlines()
    A = tuple(int(n) for n in re.findall(r"\d+", m[0]))
    B = tuple(int(n) for n in re.findall(r"\d+", m[1]))
    P = tuple(int(n) + offset for n in re.findall(r"\d+", m[2]))

    return (A, B, P)


def solve(A, B, P):
    # Set of two equations, fully determined
    # xa a + xb b = xp
    # ya a + yb b = yp

    # Can be solved analytically
    # - xa yb b + xa yp + ya xb b = ya xp
    # b = (xa yp - ya xp) / (xa yb - ya xb)
    xa, ya = A
    xb, yb = B
    xp, yp = P

    b = (xa * yp - ya * xp) / (xa * yb - ya * xb)
    if int(b) != b:
        return 0

    a = (xp - xb * b) / xa
    if int(a) != a:
        return 0

    return int(a) * 3 + int(b) * 1


machines = [parse_machine(m) for m in rawlist]


print("Part 1:\t", sum(solve(*machine) for machine in machines))

offset = 10000000000000
machines = [parse_machine(m, offset=offset) for m in rawlist]
print("Part 2:\t", sum(solve(*machine) for machine in machines))
