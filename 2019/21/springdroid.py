""" Advent of Code 2019. Day 21: Springdroid Adventure """

from intcode import run

with open("input.txt") as f:
    program = [int(n) for n in f.read().strip().split(",")]

def to_ascii(string):
    return [ord(c) for c in string] + [10]


def create_view(program, springscript):
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
            break
    return view

def print_view(view):
    for l in view:
        print(''.join(l))


"""
Comments on the springscript for Part 1

NOT A J
Sets J to True if there's a hull 1 step ahead

NOT B T
Sets T to True if there's a hull 2 steps ahead

OR T J
Sets J to True if there's a hull either 1 or 2 steps ahead

NOT C T
Sets T to True if there's a hull 3 steps ahead

OR T J
Sets J to True if there's a hull either 1, 2, or 3 steps ahead

AND D J
Finally, assert that D is ground in order to jump
Sets J to True if any of 1, 2, 3 steps ahead was a hull AND we can safely land
"""

springscript = """\
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J 
WALK
"""
view = create_view(program, springscript)
if isinstance(view, int):
    print("Part 1:\t", view)
else:
    print_view(view)


"""

     @   @   @
    @ @ @ @ @ @
   @   @   @   @ 
####.#.#..##.###
 XABCDEFGHI
The decision to jump was made at the X,
but it failed because it didn't attempt jumping again after
Ideally, it should wait 2 more steps
Perhaps if we delay jumping the longest, that's the best?

    @   @   @
   @ @ @ @ @ @
  @   @   @   @ 
####.##.#.##.###
      XABCDEFGHI

   @   @   @
  @ @ @ @ @ @
 @   @   @   @ 
####.##..#...###
 XABCDEFGHI
Should jump 1 step earlier than current program

     @     @
    @ @   @ @
   @   @@@   @ 
####...####..###
   XABCDEFGHI
"""

springscript = """\
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
AND H J
RUN
"""
view = create_view(program, springscript)
if isinstance(view, int):
    print("Part 2:\t", view)
else:
    print_view(view)
