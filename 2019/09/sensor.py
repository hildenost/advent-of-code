from intcode import run

test = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99] + [
    0
] * 100
run(test)

test = [1102, 34915192, 34915192, 7, 4, 7, 99, 0] + [0] * 100
run(test)

test = [104, 1125899906842624, 99] + [0] * 100
run(test)

from input_prog import input_program

part1_prog = [i for i in input_program] + [0] * 100
running = run(part1_prog)
next(running)
print(running.send(1))

part2_prog = [i for i in input_program] + [0] * 1000
running = run(part2_prog)
next(running)
print(running.send(2))
