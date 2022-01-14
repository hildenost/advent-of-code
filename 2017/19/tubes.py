""" Advent of Code 2017. Day 19: A Series of Tubes """

with open("input.txt") as f:
    routes = f.read().splitlines()

x, y = (routes[0].index("|"), 0)
dx, dy = 0, 1

letters = ""
steps = 0
while True:
    x += dx
    y += dy
    steps += 1

    if routes[y][x] in ["|", "-"]:
        # Don't change direction
        continue
    elif routes[y][x].isalpha():
        # Collect letter
        letters += routes[y][x]
    elif routes[y][x] == "+":
        # Crossroads!
        if dx:
            dx = 0
            for dy in (-1, 1):
                if routes[y + dy][x] == "|" or routes[y + dy][x].isalpha():
                    break
        else:
            dy = 0
            for dx in (-1, 1):
                if routes[y][x + dx] == "-" or routes[y][x + dx].isalpha():
                    break
    else:
        break
print("Part 1:\t", letters)
print("Part 2:\t", steps)

