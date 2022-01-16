""" Advent of Code 2017. Day 22: Sporifica Virus """


infected = {(-1,0), (1, 1)}

with open("input.txt") as f:
    raw_map = f.read().splitlines()


def get_initial(raw_map):
    offset = len(raw_map) // 2
    return {(j - offset, i - offset)
        for i, row in enumerate(raw_map[::-1]) # flipping it because of y up positive
        for j, col in enumerate(row)
        if col == "#"
    }

def move_right(dx, dy):
    return dy, -dx

def move_left(dx, dy):
    return move_right(-dx, -dy)

x, y = 0, 0
# x-positive to the right
# y-positive up
dx, dy = 0, 1
bursts = 0
infected = get_initial(raw_map)
for __ in range(10000):
    dx, dy = move_right(dx, dy) if (x, y) in infected else move_left(dx, dy)

    if (x, y) in infected:
        infected.remove((x, y))
    else:
        infected.add((x,y))
        bursts += 1

    x += dx
    y += dy

print("Part 1:\t", bursts)

x, y = 0, 0
# x-positive to the right
# y-positive up
dx, dy = 0, 1
bursts = 0
infected = get_initial(raw_map)
weakened = set()
flagged = set()
for __ in range(10000000):
    dx, dy = (move_right(dx, dy) if (x, y) in infected else
             (dx, dy) if (x, y) in weakened else
             (-dx, -dy) if (x, y) in flagged else
             move_left(dx, dy))

    if (x, y) in infected:
        infected.remove((x, y))
        flagged.add((x, y))
    elif (x, y) in weakened:
        weakened.remove((x, y))
        infected.add((x,y))
        bursts += 1
    elif (x, y) in flagged:
        flagged.remove((x, y))
    else: # clean
        weakened.add((x,y))

    x += dx
    y += dy

print("Part 2:\t", bursts)
