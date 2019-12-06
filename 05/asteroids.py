from input_prog import input_program

def get_value(program, immediate_mode, p):
    return program[p] if immediate_mode else program[program[p]]

def run(program, input_value=0):
    p = 0
    while True:
        instruction = str(program[p])
        third = 0 if len(instruction) < 5 else int(instruction[0])
        second = 0 if len(instruction) < 4 else int(instruction[-4])
        first = 0 if len(instruction) < 3 else int(instruction[-3])
        opcode = int(instruction[-2:])

        if opcode == 99:
            print("EXITING")
            break

        if opcode not in {3, 4}:
            a = get_value(program, first, p + 1)
            b = get_value(program, second, p + 2)
            pointer = (p + 3) if third else program[p + 3]

        if opcode == 1:
            program[pointer] = a + b
            p += 4

        elif opcode == 2:
            program[pointer] = a * b
            p += 4

        elif opcode == 3:
            program[(p + 1) if first else program[p + 1]] = input_value
            p += 2

        elif opcode == 4:
            print(program[(p + 1) if first else program[p + 1]])
            p += 2

        elif opcode == 5:
            p = b if a else p + 3

        elif opcode == 6:
            p = b if not a else p + 3

        elif opcode == 7:
            program[pointer] = int(a < b)
            p += 4

        elif opcode == 8:
            program[pointer] = int(a == b)
            p += 4
        else:
            print("COULDN'T RECOGNIZE OPCODE ", opcode)
            break

    return program

#test_1 = [1002, 4, 3, 4, 33]
#run(test_1)

### PART 1
part1_program = [p for p in input_program]
#output = run(part1_program, input_value=1)

### PART 2
run(part1_program, 5)

### tests
# Testing whether input equals 8, returns 1 if yes, 0 if no
test_2 = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
run(test_2, 3)

# Testing whether input is less than 8, returns 1 if yes, 0 if no
test_3 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
run(test_3, 7)

# Testing in immediate mode whether input equals 8, returns 1 if yes, 0 if no
test_4 = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
run(test_4, 6)

# Testing whether input is less than 8, returns 1 if yes, 0 if no
test_5 = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
run(test_5, 8)

# Jump tests: output 0 if input was 0, otherwise 1
test_6 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
run(test_6, -3)
test_7 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
run(test_7, 0)

# Testing whether input is less than, equal or more than 8, outputting
# 999, 1000, 1001, respectively
test_8 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
run(test_8, 9)
