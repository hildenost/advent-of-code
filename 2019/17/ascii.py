from intcode import run
from input_prog import input_program

def is_intersection(view, x, y):
    return view[y][x-1:x+2] == ["#"]*3 and view[y-1][x] == "#" and view[y+1][x] == "#"

def to_ascii(string):
    return [ord(c) for c in string] + [10]

def create_view(input_program, main, A, B, C, video):
    cameras = run(input_program + [0]*10000)

    view = []
    line = []
    while True:
        try:
            output = next(cameras)
            if output is None:
                for function in [main, A, B, C]:
                    for i in to_ascii(function):
                        cameras.send(i)
                    while next(cameras) is not None:
                        pass
                cameras.send(ord(video))
                cameras.send(10)
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

### PART 1
#view = create_view(input_program)
#print_view(view)
#calibration = sum(x*y for x in range(1, len(view[0])) for y in range(1, len(view)) if is_intersection(view, x, y))
#print(calibration)

### PART 2
input_program[0] = 2
total = "A,B,A,B,C,C,B,A,B,C"
A = "L,4,R,8,L,6,L,10"
B = "L,6,R,8,R,10,L,6,L,6"
C = "L,4,L,4,L,10"
print(create_view(input_program + [0]*10000, total, A, B, C, video="n"))
