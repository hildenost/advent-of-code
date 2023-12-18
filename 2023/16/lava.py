""" Advent of Code 2023. Day 16: The Floor Will Be Lava """

with open("input.txt") as f:
    layout = f.read().splitlines()

testlayout = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""
testlayout = testlayout.splitlines()

# layout = testlayout

slash = set()
backslash = set()
vertical = set()
horizontal = set()
empty = set()

for y, row in enumerate(layout):
    for x, col in enumerate(row):
        if col == "|":
            vertical.add((x, y))
            # print(x, y, col, "VERTICAL")
        elif col == "-":
            horizontal.add((x, y))
            # print(x, y, col, "HORIZONTAL")
        elif col == "/":
            slash.add((x, y))
            # print(x, y, col, "SLASH /")
        elif col == "\\":
            backslash.add((x, y))
            # print(x, y, col, "BACKSLASH \\")
        elif col == ".":
            empty.add((x, y))
        # else:
        # print(x, y, col, "EMPTY")


move = {
    ">": lambda x, y: (x + 1, y),
    "<": lambda x, y: (x - 1, y),
    "v": lambda x, y: (x, y + 1),
    "^": lambda x, y: (x, y - 1),
}


def is_valid(x, y):
    return 0 <= x < width and 0 <= y < height


def pprint(energized, layout):
    for i in range(height):
        row = ""
        for j in range(width):
            row += "#" if (j, i) in energized else layout[i][j]
        print(row)


# bfs?
# Need the position of the beam head and direction
# First beam
width = len(layout[0])
height = len(layout)

def energize(start):
    beams = [start]

    seen = set()
    energized = set()

    while beams:
        pos, direction = beams.pop()

        energized.add(pos)
        #    pprint(energized, layout)
        #    input()

        if (pos, direction) in seen:
            continue

        seen.add((pos, direction))

        new_pos = move[direction](*pos)
        if not is_valid(*new_pos):
            # Out of bounds, dismiss
            continue

        if new_pos in vertical:
            # Vertical splitter
            # If direction is vertical ^v do nothing
            if direction in "^v":
                beams.append((new_pos, direction))
            # Else split beam in two
            else:
                beams.append((new_pos, "^"))
                beams.append((new_pos, "v"))

        elif new_pos in horizontal:
            # Horizontal splitter
            # If direction is horizontal <> do nothing
            if direction in "<>":
                beams.append((new_pos, direction))
            # Else split beam in two
            else:
                beams.append((new_pos, "<"))
                beams.append((new_pos, ">"))
        elif new_pos in slash:
            # Change direction
            forwardchange = {">": "^", "<": "v", "^": ">", "v": "<"}
            beams.append((new_pos, forwardchange[direction]))

        elif new_pos in backslash:
            # Change direction
            backwardchange = {">": "v", "<": "^", "^": "<", "v": ">"}
            beams.append((new_pos, backwardchange[direction]))
        else:
            # Empty tile
            # Continue in the same direction
            beams.append((new_pos, direction))
    # Subtracting the dummy starting point
    return len(energized) - 1


# Subtracting the dummy starting point
beam = ((-1, 0), ">")
print("Part 1:\t", energize(beam))


# Along the left/right edges
energies = []
for i in range(height):
    energies.append(energize(((-1, i), ">")))
    energies.append(energize(((width, i), "<")))

# Along the top/bottom edges
for i in range(width):
    energies.append(energize(((i, -1), "v")))
    energies.append(energize(((i, height), "^")))

print("Part 2:\t", max(energies))
