""" Advent of Code 2020 Day 8: Handheld Halting """


def parse_line(line):
    cmd, value = line.split()
    return cmd, int(value)


def create_program(instructions):
    return [parse_line(line) for line in instructions.splitlines()]


SUCCESS = 1
INFINITE_LOOP = -1


def execute_program_part1(program):
    ptr = 0
    acc = 0
    executed_instructions = set()

    while ptr < len(program):
        # Read instruction
        cmd, number = program[ptr]

        # If we've encountered this command previously
        # exit with error
        if ptr in executed_instructions:
            return acc, INFINITE_LOOP

        # Else we keep track of our newly visited command
        executed_instructions.add(ptr)

        # Action
        if cmd in ["nop"]:
            ptr += 1
        elif cmd in ["jmp"]:
            ptr += number
        elif cmd in ["acc"]:
            acc += number
            ptr += 1

    # We made it through the program!
    return acc, SUCCESS


def change_program(program):
    """ Create different programs by swapping ONE `nop` or `jmp` command with the opposite. """
    return [
        [*program[:i], ("jmp" if cmd == "nop" else "nop", number), *program[i + 1 :],]
        for i, (cmd, number) in enumerate(program)
        if cmd in ["jmp", "nop"]
    ]


def execute_program_part2(program):
    programs = change_program(program)

    # Test ALL the programs
    for program in programs:
        acc, error_code = execute_program_part1(program)
        if error_code == SUCCESS:
            return acc


test_code = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
program = create_program(test_code)
print(execute_program_part1(program))
print(execute_program_part2(program))

with open("08/input.txt") as f:
    code = f.read()

program = create_program(code)
print(execute_program_part1(program))
print(execute_program_part2(program))

