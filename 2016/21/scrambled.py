""" Advent of Code 2016. Day 21: Scrambled Letters and Hash """


ops = {
    # Swap
    # If operation is swap letter,
    # convert to indices before calling
    "swap": (lambda pwd, x, y:
        pwd[:min(x, y)] + pwd[max(x, y)] +
        pwd[min(x, y)+1:max(x, y)] +
        pwd[min(x, y)] + pwd[max(x, y)+1:]),
    "reverse": lambda pwd, x, y: pwd[:x] + pwd[x:y+1][::-1] + pwd[y+1:],
    "move": (lambda pwd, x, y:
        pwd[:x] + pwd[x+1:y+1] + pwd[x] + pwd[y+1:]
        if x < y else
        pwd[:y] + pwd[x] + pwd[y:x] + pwd[x+1:]
        ),
    # if rotate left, add negative x
    "rotate": lambda pwd, x: pwd[-x:] + pwd[:-x]

}


operations = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
""".splitlines()

with open("input.txt") as f:
    operations = f.read().splitlines()

def parse(lines):
    commands = []
    for line in lines:
        cmd, *rest = line.split()
        if cmd in ["swap", "move", "reverse"]:
            __, x, *__, y = rest
            commands.append(
                (cmd, x if not x.isnumeric() else int(x), y if not y.isnumeric() else int(y)))
        elif cmd == "rotate":
            lr, x, *__, l = rest
            if lr in ["left", "right"]:
                commands.append((cmd, -int(x) if lr == "left" else int(x)))
            else:
                commands.append((cmd, l))
    return commands

algorithm = parse(operations)

pwd = "abcdefgh"
for cmd, *args in algorithm:
    if cmd == "swap" and not isinstance(args[0], int):
        pwd = ops[cmd](pwd, pwd.index(args[0]), pwd.index(args[1]))
    elif cmd == "rotate" and not isinstance(args[0], int):
        rots = (1 + pwd.index(args[0]) + (pwd.index(args[0]) >= 4)) % len(pwd)
        pwd = ops[cmd](pwd, rots) 
    else:
        pwd = ops[cmd](pwd, *args)
print("Part 1:\t", pwd)

for cmd, *args in reversed(algorithm):
    if cmd == "swap" and not isinstance(args[0], int):
        pwd = ops[cmd](pwd, pwd.index(args[0]), pwd.index(args[1]))
    elif cmd == "rotate" and not isinstance(args[0], int):
        # HEREIN LIE THE TROUBLE I MUST UNWIND
        for i in range(len(pwd)):
            test_pwd = ops[cmd](pwd, i) 
            rots = (1 + test_pwd.index(args[0]) + (test_pwd.index(args[0]) >= 4)) % len(pwd)
            if pwd == ops[cmd](test_pwd, rots):
                pwd = test_pwd
                break
    elif cmd == "rotate" and isinstance(args[0], int):
        pwd = ops[cmd](pwd, -args[0])
    elif cmd == "move":
        pwd = ops[cmd](pwd, args[1], args[0])
    else:
        pwd = ops[cmd](pwd, *args)
print("Part 2:\t", pwd)
