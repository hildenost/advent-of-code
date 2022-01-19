""" Advent of Code 2018. Day 13: Mine Cart Madness """
import re
from itertools import cycle

with open("input.txt") as f:
    raw_map = f.read().splitlines()

def turn_right(dx, dy):
    return -dy, dx

def turn_left(dx, dy):
    return dy, -dx 

def go_straight(dx, dy):
    return dx, dy

def turn():
    """ Generator function that cycles between turns """
    for func in cycle([turn_left, go_straight, turn_right]):
        yield func

# Initialize grid and carts and taken spots
grid = {}
cart = {} 
taken = set()
for y, row in enumerate(raw_map):
    for k, m in enumerate(re.finditer(r"\S", row)):
        if m[0] in "<>^v":
            # A cart
            dx = 1 if m[0] == ">" else -1 if m[0] == "<" else 0
            dy = 1 if m[0] == "v" else -1 if m[0] == "^" else 0

            cart[k] = (m.start(), y, dx, dy, turn())
            taken.add((m.start(), y))
            grid[(m.start(), y)] = "-" if m[0] in "<>" else "|" 
        else:
            grid[(m.start(), y)] = m[0]


has_collided = False

while len(taken) > 1:
    for k, (x, y, dx, dy, T) in sorted(cart.items(), key=lambda x: (x[1][1], x[1][0])):
        if (x, y) not in taken:
            # This means that on this spot, there was a collision
            del cart[k]
            continue

        taken.remove((x, y))

        x += dx
        y += dy

        if (x, y) in taken:
            if not has_collided:
                print("Part 1:\t", f"{x},{y}")
                has_collided = True

            taken.remove((x, y))
            del cart[k]
            continue

        taken.add((x, y))

        # Gonna turn?
        if grid[(x, y)] == "\\":
                  # right turn            # left turn
            dx, dy = (-dy, dx) if dy == 0 else (dy, -dx)
        elif grid[(x, y)] == "/":
                  # left turn             # right turn
            dx, dy = (dy, -dx) if dy == 0 else (-dy, dx)
        elif grid[(x, y)] == "+":
            dx, dy = next(T)(dx, dy)

        # Update cart
        cart[k] = (x, y, dx, dy, T)

print("Part 2:\t", ",".join(str(n) for n in taken.pop()))
