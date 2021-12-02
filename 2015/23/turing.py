""" Advent of Code 2015. Day 23: Opening the Turing Lock """

with open("input.txt") as f:
    program = f.read()


def parser(program):
    commands = program.replace(",", "").splitlines()
    return [
        [int(arg) if arg[0] in "+-" else arg for arg in cmd.split()] for cmd in commands
    ]


def run(program, part=1):
    cmds = parser(program)

    # the registers
    registers = {"a": 0, "b": 0} if part == 1 else {"a": 1, "b": 0}
    # the instructions
    instructions = {
        "hlf": lambda r: registers[r]
        / 2,  # hlf r sets register r to half its current value
        "tpl": lambda r: 3
        * registers[r],  # tpl r sets register r to triple its current value
        "inc": lambda r: registers[r] + 1,  # inc r increments register r by 1
        "jmp": lambda offset: offset,  # is a jump, continuing the instruction offset away relative to self
        "jie": lambda r, offset: 1
        if registers[r] % 2
        else offset,  # like jmp, but only jump if register r is even
        "jio": lambda r, offset: 1
        if registers[r] != 1
        else offset,  # like jmp, but only jump if register r is 1
    }

    pointer = 0
    while True:
        cmd, *args = cmds[pointer]
        if cmd.startswith("j"):
            pointer += instructions[cmd](*args)
        else:
            registers[args[0]] = instructions[cmd](*args)
            pointer += 1

        if pointer >= len(cmds):
            break

    return registers["b"]


print("PART 1:\t", run(program))
print("PART 2:\t", run(program, part=2))
