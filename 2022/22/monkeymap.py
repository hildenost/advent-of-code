""" Advent of Code 2022. Day 22: Monkey Map """

with open("input.txt") as f:
    board, dirs = f.read().split("\n\n")

# Parsing the board
walls = set()
tiles = set()
for y, row in enumerate(board.split("\n")):
    for x, cell in enumerate(row):
        match cell:
            case ".":
                tiles.add((x, y))
            case "#":
                walls.add((x, y))


start = min(tiles, key=lambda x: (x[1], x[0]))

import re
pathnumbers = [int(n) for n in re.findall(r"\d+", dirs)]
turns = re.findall(r"[RL]", dirs)

turning = {
    "L": lambda x: "D" if x == "L" else "U",
    "R": lambda x: "U" if x == "L" else "D",
    "D": lambda x: "R" if x == "L" else "L",
    "U": lambda x: "L" if x == "L" else "R"
}


def peek(x, y, dx, dy):
    return x+dx, y+dy

moves = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

def wrap(tile, face):
    if face == "R":
        return min((x, y) for x, y in tiles | walls if y == tile[1])
    if face == "L":
        return max((x, y) for x, y in tiles | walls if y == tile[1])
    if face == "U":
        return max([(x, y) for x, y in tiles | walls if x == tile[0]], key=lambda x: (x[1], x[0]))
    if face == "D":
        return min([(x, y) for x, y in tiles | walls if x == tile[0]], key=lambda x: (x[1], x[0]))

face = "R"
curr = start
while True:
    steps = pathnumbers.pop(0)

    for step in range(steps):
        temp = peek(*curr, *moves[face])

        if temp in walls:
            break

        if temp in tiles:
            curr = temp
            continue

        # If we made it here, it means wrapping time!
        new_curr = wrap(temp, face)
        if new_curr in walls:
            break
        curr = new_curr

    if not turns:
        break

    face = turning[face](turns.pop(0))
    

def password(col, row, face):
    return 1000*(row+1) + 4*(col+1) + "RDLU".find(face)

print("Part 1:\t", password(*curr, face))


pathnumbers = [int(n) for n in re.findall(r"\d+", dirs)]
turns = re.findall(r"[RL]", dirs)


face = "R"
curr = start
while True:
    steps = pathnumbers.pop(0)

    for step in range(steps):
        temp = peek(*curr, *moves[face])

        if temp in walls:
            break

        if temp in tiles:
            curr = temp
            continue

        # If we made it here, it means wrapping time!
        """
            1   2

            3

        4   5

        6

        """
        # First, deciding facenumber, see sketch above
        x, y = curr
        if 50<=x<100 and 0<=y<50:
            # Face 1
            #If needing to go UP (that is, y == 0, 50<=x<100), we're wrapping to face 6, entering from 6's LEFT side.
            if face == "U":
                new_face = "R"
                new_curr = (0, x + 100)
            #If needing to go LEFT (that is, 0<=y<50, x==50), we're wrapping to face 4, entering from 4's LEFT side, but UPSIDE DOWN.
            elif face == "L":
                new_face = "R"
                new_curr = (0, -y+149)
        elif 100<=x<150 and 0<=y<50:
            # Face 2
            #If needing to go UP (that is, y == 0, 100<=x<150), we're wrapping to face 6, entering from 6's DOWN side.
            if face == "U":
                new_face = "U"
                new_curr = (x - 100, 199)
            #If needing to go RIGHT (0<=y<50, x==149), we're wrapping to face 2, entering from 5's RIGHT side, but UPSIDE DOWN.
            elif face == "R":
                new_face = "L"
                new_curr = (99, -y+149)
            #Going DOWN (y==49, 100<=x<150), wrapping to face 3, entering from 3's RIGHT side.
            elif face == "D":
                new_face = "L"
                new_curr = (99, x - 50)
        if 50<=x<100 and 50<=y<100:
            # Face 3
            #Going LEFT (50<=y<100, x==50) into face 4 from TOP side.
            if face == "L":
                new_face ="D"
                new_curr = (y-50, 100)
            #Going RIGHT (50<=y<100, x==149) into face 2 from DOWN side.
            elif face == "R":
                new_face = "U"
                new_curr = (y + 50, 49)
        elif 0<=x<50 and 100<=y<150:
            # Face 4
            #Going LEFT (100<=y<150, x==0) into face 1 from LEFT side, but UPSIDE DOWN.
            if face == "L":
                new_face = "R"
                new_curr = (50, 149 - y)
            #Going UP (y==100, 0<=x<50) into face 3 from LEFT side.
            elif face == "U":
                new_face = "R"
                new_curr = (50, x + 50)
        elif 50<=x<100 and 100<=y<150:
            # Face 5
            #Going RIGHT (100<=y<150, x==149) into face 2 from RIGHT side, but UPSIDE DOWN.
            if face == "R":
                new_face = "L"
                new_curr = (149, 149 - y)
            #Going DOWN (y==149, 50<=x<149) into face 6 from RIGHT side.
            elif face == "D":
                new_face = "L"
                new_curr = (49, x + 100)
        elif 0<=x<50 and 150<=y<200:
            #Going LEFT (150<=y<200, x==0) into face 1 from TOP side.
            if face == "L":
                new_face = "D"
                new_curr = (y - 100, 0)
            #Going RIGHT (150<=y<200, x==149) into face 5 from DOWN side.
            elif face == "R":
                new_face = "U"
                new_curr = (y - 100, 149)
            #Going DOWN (y==199, 0<=x<50) into face 2 TOP side.
            elif face == "D":
                new_face = "D"
                new_curr = (x + 100, 0)

        if new_curr in walls:
            break
        curr = new_curr
        face = new_face

    if not turns:
        break

    face = turning[face](turns.pop(0))

print("Part 2:\t", password(*curr, face))
