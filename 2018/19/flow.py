""" Advent of Code 2018. Day 19: Go With The Flow """
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
    "eqrr": lambda a, b, regs: int(regs[a] == regs[b]),
}


def run(program, ip=0, v=0, to_return=0, stop_at=None):
    if stop_at == None:
        stop_at = len(program)

    regs = [0, 0, 0, 0, 0, 0]
    regs[0] = v

    while regs[ip] < len(program):
        cmd, a, b, c = program[regs[ip]]
        regs[c] = opcodes[cmd](a, b, regs)

        regs[ip] += 1

        if regs[ip] == stop_at:
            return regs[to_return]
    return regs[to_return]


def parse(instructions):
    ip = int(instructions[0].split()[1])

    program = [
        tuple(int(n) if n.isdigit() else n for n in line.split())
        for line in instructions[1:]
    ]

    return program, ip


with open("input.txt") as f:
    instructions = f.read().splitlines()

program, ip = parse(instructions)
print("Part 1:\t", run(program, ip))

# After inspecting the code, it seems that after initialising the value in
# register 2 (1030 in part 1, 10 551 430 in part 2),
# the program sums all factors of the number in register 2
import math


def sum_factors(number):
    n = math.floor(math.sqrt(number))
    total = 0
    for i in range(1, n):
        if number % i == 0:
            total += i + number // i
    return total


# First, we make the program return register 2 after initialising has finished,
# Then, we compute the sum of factors with our own program
print("Part 2:\t", sum_factors(run(program, ip=ip, v=1, to_return=2, stop_at=1)))
