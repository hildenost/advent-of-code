""" Advent of Code 2018. Day 21: Chronal Conversion """

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

    tracker = []

    while regs[ip] < len(program):
        cmd, a, b, c = program[regs[ip]]

        if cmd == "eqrr" and regs[5] in tracker:
            return tracker[0:2], tracker[-1]

        if cmd == "eqrr":
            print(regs[5], len(tracker))
            tracker.append(regs[5])

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


# Inspecting the program first
# The only command that uses register 0, is
# eqrr 5 0 3
# That is, if regs[5] == regs[0]
# the program halts, because regs[ip] is jumping out

# So, let's monitor regs[5]
# But I rewrote it because the assembly was slow
# regs = run(program, ip)


def solve():
    tracker = []
    e = 0
    while e not in tracker:
        tracker.append(e)

        b = e | 65536
        e = 4591209
        while True:
            d = b & 255
            e += d
            e &= 16777215
            e *= 65899
            e &= 16777215

            if 256 > b:
                break

            b //= 256

    # tracker[0] is 0, which is not an option
    return tracker[1], tracker[-1]


least, most = solve()

print("Part 1:\t", least)
print("Part 2:\t", most)
