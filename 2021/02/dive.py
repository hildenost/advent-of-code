""" Advent of Code 2021. Day 2: Dive! """


with open("input.txt") as f:
    course = [c.split() for c in f.read().splitlines()]

cmd1 = {
    "forward": lambda x, d, p, aim: (d, p + x, aim),
    "down": lambda x, d, p, aim: (d + x, p, aim),
    "up": lambda x, d, p, aim: (d - x, p, aim),
}
cmd2 = {
    "forward": lambda x, d, p, aim: (d + aim * x, p + x, aim),
    "down": lambda x, d, p, aim: (d, p, aim + x),
    "up": lambda x, d, p, aim: (d, p, aim - x),
}


def drive(course, commands):
    # args = (depth, position, aim)
    args = (0, 0, 0)
    for cmd, x in course:
        args = commands[cmd](int(x), *args)
    return args[0] * args[1]


print("Part 1:\t", drive(course, commands=cmd1))
print("Part 2:\t", drive(course, commands=cmd2))
