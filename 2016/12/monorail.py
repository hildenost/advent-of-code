""" Advent of Code 2016. Day 12: Leonardo's Monorail """


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
    return [[x if not (x.isnumeric() or x[0] == "-") else int(x) for x in line.split()] for line in program]

program = parse(program)

def run(program, part=1):
    regs = {k: 0 for k in "abcd"}
    regs["c"] = 1 if part == 2 else 0
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
            x, = args
            regs[x] += 1
            i += 1
        elif cmd == "dec":
            x, = args
            regs[x] -= 1
            i += 1
        elif cmd == "jnz":
            x, y = args
            if isinstance(x, int) and x != 0:
                i += y
                continue
            elif regs[x] != 0:
                i += y
                continue
            else:
                i += 1
    return regs["a"]

print("Part 1:\t", run(program))
print("Part 2:\t", run(program, part=2))

