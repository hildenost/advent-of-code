""" Advent of Code 2016. Day 23: Safe Cracking """


input_program = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
""".splitlines()
with open("input.txt") as f:
    input_program = f.read().splitlines()


def parse(program):
    return [
        [x if not (x.isnumeric() or x[0] == "-") else int(x) for x in line.split()]
        for line in program
    ]


def run(program, a=0):
    regs = {k: 0 for k in "abcd"}
    regs["a"] = a
    i = 0
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
            if not isinstance(y, int):
                y = regs[y]

            if not isinstance(x, int):
                x = regs[x]

            if x != 0:
                i += y
                continue
            else:
                i += 1
        elif cmd == "mul":
            x, y = args

            if not isinstance(x, int):
                x = regs[x]

            regs[y] = regs[y] * x
            i += 1

        elif cmd == "tgl":
            (x,) = args
            if not isinstance(x, int):
                x = regs[x]

            if not 0 <= i + x < len(program):
                i += 1
                continue

            pointer = program[i + x]
            if pointer[0] == "inc":
                pointer[0] = "dec"
            elif pointer[0] in ["dec", "tgl"]:
                pointer[0] = "inc"
            elif pointer[0] == "jnz":
                pointer[0] = "cpy"
            elif pointer[0] in ["cpy", "mul"]:
                pointer[0] = "jnz"

            i += 1

    return regs["a"]


program = parse(input_program)
print("Part 1:\t", run(program, a=7))
program = parse(input_program)
# Noticing some multiplication ops from the hint in Part 2
# Tweaking the program a bit
program[3] = ["mul", "b", "a"]
program[5] = ["cpy", 0, "c"]
program[6] = ["cpy", 0, "d"]
noop = ["jnz", 0, 0]
program[7] = noop
program[8] = noop
program[9] = noop
# I can probably tweak more, but it was fast enough
print("Part 2:\t", run(program, a=12))

