""" Advent of Code 2016. Day 25: Clock Signal """

program = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
""".splitlines()
with open("input.txt") as f:
    program = f.read().splitlines()


def parse(program):
    return [
        [x if not (x.isnumeric() or x[0] == "-") else int(x) for x in line.split()]
        for line in program
    ]


program = parse(program)

import re


def repeated(s):
    match = re.match(r"(.+?)\1\1\1+$", s)
    return match[1] if match else None


def run(program, a=0):
    regs = {k: 0 for k in "abcd"}
    regs["a"] = a
    i = 0
    output = ""
    while i < len(program):
        cmd, *args = program[i]
        if cmd == "cpy":
            x, y = args
            if isinstance(x, int):
                regs[y] = x
            else:
                regs[y] = regs[x]
            i += 1
        elif cmd == "inc":
            (x,) = args
            regs[x] += 1
            i += 1
        elif cmd == "dec":
            (x,) = args
            regs[x] -= 1
            i += 1
        elif cmd == "jnz":
            x, y = args
            if isinstance(x, int):
                if x != 0:
                    i += y
                else:
                    i += 1
            elif regs[x] != 0:
                i += y
                continue
            else:
                i += 1
        elif cmd == "out":
            (x,) = args
            if isinstance(x, int):
                output += str(x)
            else:
                output += str(regs[x])
            i += 1
            repeat = repeated(output)
            if repeat is not None:
                if repeat == "01":
                    return a
                return None
    return regs["a"]


res = None
i = 0
while res is None:
    i += 1
    res = run(program, a=i)


print("Part 1:\t", res)

