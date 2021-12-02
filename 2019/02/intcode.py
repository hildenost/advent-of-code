from input_prog import input_program

def run(program):
    p = 0
    while True:
        if program[p] == 1:
            program[program[p + 3]] = program[program[p + 1]] + program[program[p + 2]]
        elif program[p] == 2:
            program[program[p + 3]] = program[program[p + 1]] * program[program[p + 2]]
        elif program[p] == 99:
            return program
        else:
            print("ILLEGAL OPCODE ", program[p])
            break
        p += 4
    return program


### TESTS
test_program1 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
test_program2 = [1, 0, 0, 0, 99]
test_program3 = [2, 3, 0, 3, 99]
test_program4 = [2, 4, 4, 5, 99, 0]
test_program5 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
assert run(test_program1) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
assert run(test_program2) == [2, 0, 0, 0, 99]
assert run(test_program3) == [2, 3, 0, 6, 99]
assert run(test_program4) == [2, 4, 4, 5, 99, 9801]
assert run(test_program5) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

### PART 1
part1_program = [p for p in input_program]
part1_program[1] = 12
part1_program[2] = 2
output = run(part1_program)
print(output[0])

### PART 2
output_halt = 19690720
for noun in range(100):
    for verb in range(100):
        test_program = [p for p in input_program]
        test_program[1] = noun
        test_program[2] = verb
        if run(test_program)[0] == output_halt:
            print(100*noun + verb)
            break

