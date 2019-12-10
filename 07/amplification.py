"""Day 7: Amplification Circuit

Uses partials and python coroutines with yield and send.
"""

from functools import partial
from itertools import permutations

def get_value(program, immediate_mode, p):
    return program[p] if immediate_mode else program[program[p]]

def run(program, setting=0, setting_done=True):
    p = 0
    output_value = 0
    while True:
        instruction = str(program[p])

        third = 0 if len(instruction) < 5 else int(instruction[0])
        second = 0 if len(instruction) < 4 else int(instruction[-4])
        first = 0 if len(instruction) < 3 else int(instruction[-3])
        opcode = int(instruction[-2:])

        if opcode == 99:
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
            if setting_done:
                program[(p + 1) if first else program[p + 1]] = yield
            else:
                program[(p + 1) if first else program[p + 1]] = setting
            setting_done = True
            p += 2

        elif opcode == 4:
            output_value = program[(p + 1) if first else program[p + 1]]
            yield output_value
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

    return output_value

def amplify(main_program, phase_sequence):

    # Deep copying programs
    programA = [t for t in main_program]
    programB = [t for t in main_program]
    programC = [t for t in main_program]
    programD = [t for t in main_program]
    programE = [t for t in main_program]

    # Set up each individual run
    runA = partial(run, programA, setting_done=False, setting=phase_sequence[0])
    runB = partial(run, programB, setting_done=False, setting=phase_sequence[1])
    runC = partial(run, programC, setting_done=False, setting=phase_sequence[2])
    runD = partial(run, programD, setting_done=False, setting=phase_sequence[3])
    runE = partial(run, programE, setting_done=False, setting=phase_sequence[4])

    # Collect and initialize tasks
    tasks = [runA(), runB(), runC(), runD(), runE()]
    for t in tasks:
        next(t)

    output = 0
    while tasks:
        task = tasks.pop(0)
        try:
            output = task.send(output)
            next(task) # Need to move to next yield
            tasks.append(task)
        except StopIteration:
            task.close()
    return output

def test_settings(main_program, start, stop):
    return max(
        amplify(main_program, settings)
        for settings in permutations(range(start, stop))
    )

main_program = [3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99]

### PART 1
print(test_settings(main_program, 0, 5))
### PART 2
print(test_settings(main_program, 5, 10))

### TESTS
test_1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
assert 43210 == amplify(test_1, [4, 3, 2, 1, 0])
assert 40312 == amplify(test_1, [4, 0, 3, 1, 2])

test_2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]
assert 54321 == amplify(test_2, [0, 1, 2, 3, 4])

test_3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
assert 65210 == amplify(test_3, [1, 0, 4, 3, 2])

test_4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
assert 139629729 == amplify(test_4, [9, 8, 7, 6, 5])

test_5 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
assert 18216 == amplify(test_5, [9, 7, 8, 5, 6])
