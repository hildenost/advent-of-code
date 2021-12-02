def get_pointer(program, p, mode, r):
    return p if mode == 1 else r + program[p] if mode == 2 else program[p]


OPCODES = {
    1: lambda x, y, p: (x + y, p + 4),
    2: lambda x, y, p: (x * y, p + 4),
    5: lambda x, y, p: (None, y if x else p + 3),
    6: lambda x, y, p: (None, y if not x else p + 3),
    7: lambda x, y, p: (int(x < y), p + 4),
    8: lambda x, y, p: (int(x == y), p + 4),
}


def run(program, input_value=0):
    p = 0
    r = 0

    while True:
        instruction = str(program[p])

        third = 0 if len(instruction) < 5 else int(instruction[0])
        second = 0 if len(instruction) < 4 else int(instruction[-4])
        first = 0 if len(instruction) < 3 else int(instruction[-3])

        opcode = int(instruction[-2:])

        if opcode == 99:
            break

        a = (
            program[get_pointer(program, p + 1, first, r)]
            if opcode not in {3, 4}
            else input_value
        )
        b = (
            program[get_pointer(program, p + 2, second, r)]
            if opcode not in {3, 4, 9}
            else 0
        )
        pointer = (
            get_pointer(program, p + 3, third, r)
            if opcode not in {3, 4, 9}
            else get_pointer(program, p + 1, first, r)
        )

        if opcode in {1, 2, 7, 8}:
            program[pointer], p = OPCODES[opcode](a, b, p)

        elif opcode in {5, 6}:
            __, p = OPCODES[opcode](a, b, p)

        elif opcode == 3:
            input_value = yield
            program[pointer] = input_value
            p += 2

        elif opcode == 4:
            output_value = program[pointer]
            yield output_value
            p += 2

        elif opcode == 9:
            r += a
            p += 2

        else:
            print("COULDN'T RECOGNIZE OPCODE ", opcode)
            break

    return program
