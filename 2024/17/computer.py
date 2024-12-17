def get_pointer(program, p, mode, r):
    return p if mode == 1 else r + program[p] if mode == 2 else program[p]


OPCODES = {
    0: lambda a, combo, p: (a // 2**combo, p + 2),  # adv
    1: lambda b, literal, p: (b ^ literal, p + 2),  # bxl
    2: lambda _, combo, p: (combo % 8, p + 2),  # bst
    3: lambda a, literal, p: (None, literal if a else p + 2),  # jnz
    4: lambda b, c, p: (b ^ c, p + 2),  # bxc
    5: lambda _, combo, p: (combo % 8, p + 2),  # out
    6: lambda a, combo, p: (a // 2**combo, p + 2),  # bdv
    7: lambda a, combo, p: (a // 2**combo, p + 2),  # cdv
}


def combos(i, A, B, C):
    return [0, 1, 2, 3, A, B, C, None][i]


def run(program, A=None, B=None, C=None, debug=False):
    p = 0

    output = []
    i = 0

    while p < len(program):
        opcode = program[p]
        operand = program[p + 1]

        if opcode in {0, 2, 5, 6, 7}:
            value, p = OPCODES[opcode](A, combos(operand, A, B, C), p)

        if opcode in {1}:
            value, p = OPCODES[opcode](B, operand, p)

        if opcode in {3}:
            __, p = OPCODES[opcode](A, operand, p)

        if opcode in {4}:
            value, p = OPCODES[opcode](B, C, p)

        if opcode in {0}:
            # Write to A
            A = value

        if opcode in {1, 2, 4, 6}:
            # Write to B
            B = value

        if opcode in {7}:
            # Write to C
            C = value

        if opcode in {5}:
            # Write to out
            output.append(str(value))

    return output
