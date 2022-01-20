""" Advent of Code 2018. Day 16: Chronal Classification """

with open("input.txt") as f:
    samples, program = f.read().split("\n\n\n")

opcodes = {
    "addr": lambda a, b, regs: regs[a] + regs[b],
    "addi": lambda a, b, regs: regs[a] + b,
    "mulr": lambda a, b, regs: regs[a] * regs[b],
    "muli": lambda a, b, regs: regs[a] * b,
    "banr": lambda a, b, regs: regs[a] & regs[b],
    "bani": lambda a, b, regs: regs[a] & b,
    "borr": lambda a, b, regs: regs[a] | regs[b],
    "bori": lambda a, b, regs: regs[a] | b,
    "setr": lambda a, b, regs: regs[a],
    "seti": lambda a, b, regs: a,
    "gtir": lambda a, b, regs: int(a > regs[b]),
    "gtri": lambda a, b, regs: int(regs[a] > b),
    "gtrr": lambda a, b, regs: int(regs[a] > regs[b]),
    "eqir": lambda a, b, regs: int(a == regs[b]),
    "eqri": lambda a, b, regs: int(regs[a] == b),
    "eqrr": lambda a, b, regs: int(regs[a] == regs[b])
}


import re

options = []
counter = 0
for sample in samples.split("\n\n"):
    sample = [int(n) for n in re.findall(r"\d+", sample)]

    regs = sample[:4]
    cmd, a, b, c = sample[4:8]
    new_regs = sample[8:]

    res = {(op, cmd) for op in opcodes if new_regs[c] == opcodes[op](a, b, regs)}

    options.append(res)
    counter += len(res) >= 3

print("Part 1:\t", counter)

codes = [None]*16
while options:
    shortest = min(options, key=len)

    if len(shortest) == 1:
        cmd, value = shortest.pop()
        codes[value] = cmd

        # Then remove this command from all other samples
        options = [{(k, v) for k, v in o if k not in codes}
            for o in options]
        options = [o for o in options if len(o) > 0]


program = [tuple(int(n) for n in line.split()) 
                        for line in program.strip().splitlines()]

def run(program):
    regs = [0, 0, 0, 0]
    for cmd, a, b, c in program:
        regs[c] = opcodes[codes[cmd]](a, b, regs)
    return regs[0]

print("Part 2:\t", run(program))

