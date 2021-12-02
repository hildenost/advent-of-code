""" Advent of Code 2021. Day 2: Dive! """


with open("input.txt") as f:
    course = [c.split() for c in f.read().splitlines()]

cmd1 = {
    "forward": lambda x, d, p: (d, p + x),
    "down": lambda x, d, p: (d + x, p),
    "up": lambda x, d, p: (d - x, p),
}
cmd2 = {
    "forward": lambda x, d, p, aim: (d + aim * x, p + x, aim),
    "down": lambda x, d, p, aim: (d, p, aim + x),
    "up": lambda x, d, p, aim: (d, p, aim - x),
}


def drive(course, part=1):
    args = (0, 0) if part == 1 else (0, 0, 0)
    commands = cmd1 if part == 1 else cmd2
    for cmd, x in course:
        args = commands[cmd](int(x), *args)
    return args[0] * args[1]


print("Part 1:\t", drive(course))
print("Part 2:\t", drive(course, part=2))
