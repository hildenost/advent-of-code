""" Advent of Code 2019. Day 21: Springdroid Adventure """

from intcode import run

with open("input.txt") as f:
    program = [int(n) for n in f.read().strip().split(",")]

def to_ascii(string):
    return [ord(c) for c in string] + [10]

def run_script(program, springscript):
    b = run(program + [0]*10000)

    view = []
    line = []
    while True:
        try:
            output = next(b)
            if output is None:
                for function in springscript.splitlines():
                    for i in to_ascii(function):
                        b.send(i)
            elif output == 10:
                view.append(line)
                line = []
            elif output < 256:
                line.append(chr(output))
            else:
                return output
        except StopIteration:
            for l in view:
                print(''.join(l))
            return "FELL INTO HOLE"

"""
Comments on the springscript for Part 1
OR A T      // T is False if A is hole
AND B T     // T is False if A or B is hole
AND C T     // T is False if previous T or C are holes
NOT T J     // If T is False, we want to jump
AND D J     // But D must be ground so we can land safely
"""

springscript = """\
OR A T
AND B T
AND C T
NOT T J
AND D J 
WALK
"""
print("Part 1:\t", run_script(program, springscript))

"""
General rules for part 2:

In order to jump
    - the first jump (part 1) must be valid
    AND
    - the first jump should not make subsequent jumps impossible 

This means that E and H cannot be holes at the same time. (Or F and I, but
it work with just E and H.)
"""
springscript = """\
OR A T
AND B T
AND C T
NOT T T
AND D T
OR H J
OR E J
AND T J
RUN
"""
print("Part 2:\t", run_script(program, springscript))
