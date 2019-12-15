from input_prog import input_program
from intcode import run

### PART 1
def count_blocks(program):
    game = run(program + [0]*1000)
    outputs = [o for o in game]
    xs = (o for o in outputs[::3])
    ys = (o for o in outputs[1::3])
    tiles = (o for o in outputs[2::3])
    return sum(t == 2 for t in tiles)

print(count_blocks(input_program))


### PART 2
def render_screen(screen, X, Y, curr_score, out_screen=None):
    xs = [o for o in screen[::3]]
    ys = [o for o in screen[1::3]]
    symbols = {
        0: " ",
        1: "#",
        2: "*",
        3: "~",
        4: "o"
    }
    tiles = (symbols[o] if o in symbols else o for o in screen[2::3])

    if out_screen is None:
        out_screen = [[None]*X for __ in range(Y)]

    for x, y, r in zip(xs, ys, tiles):
        if x == -1 and y == 0:
            curr_score = r
        else:
            out_screen[y][x] = r

    return out_screen, curr_score

def print_screen(out_screen, curr_score):
    for row in out_screen:
        print(''.join(row))
    print("\tCURRENT SCORE\t", curr_score)

def get_move():
    key = input("MOVE: left [j], stay [enter], right [k], exit(q) > ")
    while key not in "j kq":
        key = input("MOVE: left [j], stay [enter], right [k], exit(q) > ")
    if key == "q":
        print("QUITTING GAME. BYE!")
        exit()
    moves = {"j": -1, "k": 1, "": 0}
    return moves[key]

def get_move_ai(out_screen):
    for y, row in enumerate(out_screen):
        for x, tile in enumerate(row):
            if tile == "o":
                ball = x
            elif tile == "~":
                paddle = x
    if ball < paddle:
        return -1
    elif ball > paddle:
        return 1
    else:
        return 0



input_program[0] = 2
X, Y = (37, 23)

# Initialization: Initial board render
game = run(input_program + [0]*1000)
screen = [next(game) for __ in range(X*Y*3 + 3)]
out_screen, score = render_screen(screen, X, Y, 0)

while True:
    try:
        turn = next(game)
    except StopIteration:
        print("GAME OVER!")
        print_screen(out_screen, score)
        exit()
    if turn is None:
        move = get_move_ai(out_screen)
        turn = game.send(move)
    screen = [turn] + [next(game) for __ in range(2)]
    out_screen, score = render_screen(screen, X, Y, score, out_screen)

