from intcode import run
from input_prog import paint_program

right_turns = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}
left_turns = {
    "^": "<",
    "<": "v",
    "v": ">",
    ">": "^",
}
moves = {
    "v": lambda x, y: (x, y+1),
    ">": lambda x, y: (x+1, y),
    "^": lambda x, y: (x, y-1),
    "<": lambda x, y: (x-1, y),
}

def paint(part2=False):
    panels = [[0]*70 for i in range(50)]

    x, y = 5, 5
    panels[y][x] = part2
    face = "^"

    # Deep copying programs
    color_program = [t for t in paint_program] + [0]*1000

    # Set up each individual run
    robot = run(color_program)

    # Initialize tasks
    next(robot)

    squares = {(x, y)}
    output = 0
    i = 0
    while True:
        try:
            input_value = panels[y][x]
            output = robot.send(input_value)
            panels[y][x] = output
            output_value = next(robot) # Need to move to next yield
            turn_right = output_value
            face = right_turns[face] if turn_right else left_turns[face]
            x, y = moves[face](x, y)
            squares.add((x, y))
            next(robot)
        except StopIteration:
            robot.close()
            break
    return panels if part2 else len(squares)

### PART 1
print(paint())

### PART 2
panels = paint(part2=True)
for p in panels:
    print(''.join("#" if c else " " for c in p))
