""" Advent of Code 2017. Day 23: Coprocessor Conflagration """

def run(program, debug=False):
    regs = {k: 0 for k in "abcdefgh"}

    if not debug:
        regs["a"] = 1

    ops = {
        "set": lambda x, y: y,
        "sub": lambda x, y: regs[x] - y,
        "mul": lambda x, y: regs[x] * y,
        "jnz": lambda x, y: y if x != 0 else 1,
    }

    p = 0

    mul_count = 0
    while p < len(program):
        cmd, *args = program[p]

        if cmd == "mul":
            mul_count += 1

        x, y = args
        y = int(y) if y.isdigit() or y[0] == "-" else regs[y]

        if cmd == "jnz":
            x = int(x) if x.isdigit() or x[0] == "-" else regs[x]
            p += ops[cmd](x, y)
            continue

        regs[x] = ops[cmd](x, y)
        p += 1

    return mul_count if debug else regs["h"]

with open("input.txt") as f:
    program = [line.split() for line in f.read().splitlines()]

print("Part 1:\t", run(program, debug=True))

# h is increased anytime b is not a prime
# counting upwards from 106700 to 123700
# in 17 size steps
import math
def has_factors(number):
    for n in range(2, math.floor(math.sqrt(number))):
        if number % n == 0:
            return True
    return False

print("Part 2:\t", sum(has_factors(b) for b in range(106700, 123701, 17)))


