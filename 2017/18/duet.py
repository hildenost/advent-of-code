""" Advent of Code 2017. Day 18: Duet """
from collections import defaultdict

with open("input.txt") as f:
    program = [line.split() for line in f.read().splitlines()]


def run1(program, pid=0):
    regs = defaultdict(int)
    regs["p"] = pid

    ops = {
        "set": lambda x, y: y,
        "add": lambda x, y: regs[x] + y,
        "mul": lambda x, y: regs[x] * y,
        "mod": lambda x, y: regs[x] % y,
        "jgz": lambda x, y: y if x > 0 else 1,
    }

    p = 0
    while True:
        cmd, *args = program[p]

        if cmd in ["snd", "rcv"]:
            (x,) = args
            x = int(x) if x.isdigit() or x[0] == "-" else regs[x]
        else:
            x, y = args
            y = int(y) if y.isdigit() or y[0] == "-" else regs[y]

        if cmd == "snd":
            sound = x
        elif cmd == "rcv":
            if x != 0:
                return sound
        elif cmd == "jgz":
            x = int(x) if x.isdigit() or x[0] == "-" else regs[x]

            p += ops[cmd](x, y)
            continue
        else:
            regs[x] = ops[cmd](x, y)

        p += 1


print("Part 1:\t", run1(program))


def run2(program, pid=0):
    regs = defaultdict(int)
    regs["p"] = pid

    ops = {
        "set": lambda x, y: y,
        "add": lambda x, y: regs[x] + y,
        "mul": lambda x, y: regs[x] * y,
        "mod": lambda x, y: regs[x] % y,
        "jgz": lambda x, y: y if x > 0 else 1,
    }

    p = 0
    while 0 <= p < len(program):
        cmd, *args = program[p]

        if cmd == "snd":
            (x,) = args
            x = int(x) if x.isdigit() or x[0] == "-" else regs[x]
        elif cmd == "rcv":
            (x,) = args
        else:
            x, y = args
            y = int(y) if y.isdigit() or y[0] == "-" else regs[y]

        if cmd == "snd":
            yield x
        elif cmd == "rcv":
            a = yield
            while a is None:
                a = yield
            regs[x] = a
        elif cmd == "jgz":
            x = int(x) if x.isdigit() or x[0] == "-" else regs[x]

            p += ops[cmd](x, y)
            continue
        else:
            regs[x] = ops[cmd](x, y)

        p += 1


programs = [run2(program, pid=0), run2(program, pid=1)]

queue_a = []
queue_b = []

a = next(programs[0])
b = next(programs[1])
times = 0
while True:
    while a is not None:
        queue_a.append(a)
        a = next(programs[0])

    while queue_b and a is None:
        a = programs[0].send(queue_b.pop(0))
        times += 1

    while b is not None:
        queue_b.append(b)
        b = next(programs[1])

    while queue_a and b is None:
        b = programs[1].send(queue_a.pop(0))

    if b is None and a is None:
        break
print("Part 2:\t", times)
