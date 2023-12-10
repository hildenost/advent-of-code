""" Advent of Code 2023. Day 10: Pipe Maze """

with open("input.txt") as f:
    lines = f.readlines()

testlines = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".splitlines()

# lines = testlines

width = len(lines[0])
height = len(lines)

tiles = dict()
for y, line in enumerate(lines):
    for x, tile in enumerate(line):
        if tile == "S":
            start = (x, y)
            tiles[(x, y)] = tile

        elif tile != ".":
            tiles[(x, y)] = tile


def can_up(x, y):
    return y > 0 and tiles[(x, y)] in "JL|S" and tiles[(x, y - 1)] in "7F|"


def can_down(x, y):
    return y < height and tiles[(x, y)] in "7F|S" and tiles[(x, y + 1)] in "JL|"


def can_left(x, y):
    return x > 0 and tiles[(x, y)] in "-J7S" and tiles[(x - 1, y)] in "-FL"


def can_right(x, y):
    return x < width and tiles[(x, y)] in "-FLS" and tiles[(x + 1, y)] in "-J7"


pos = start
seen = []
while True:
    x, y = pos
    seen.append(pos)

    if can_up(x, y) and (x, y - 1) not in seen:
        pos = (x, y - 1)
    elif can_down(x, y) and (x, y + 1) not in seen:
        pos = (x, y + 1)
    elif can_right(x, y) and (x + 1, y) not in seen:
        pos = (x + 1, y)
    elif can_left(x, y) and (x - 1, y) not in seen:
        pos = (x - 1, y)
    else:
        print("Part 1:\t", len(seen) // 2)
        break

inside = 0
ins = set()
for y, line in enumerate(lines):
    edges = 0
    bend = None
    for x, tile in enumerate(line):
        if (x, y) in seen:
            if bend == "F" and tile == "7":
                edges -= 1
            elif bend == "L" and tile == "J":
                edges -= 1
            elif tile in "|":
                edges += 1
            elif tile in "FL":
                bend = tile
                edges += 1
        elif edges % 2:
            ins.add((x, y))
            inside += 1

print("Part 2:\t", inside)

box = {
    "J": "\u255D",
    "L": "\u255A",
    "F": "\u2554",
    "7": "\u2557",
    "-": "\u2550",
    "|": "\u2551",
}


def printmaze(current=None, inside=False):
    for y in range(height):
        row = ""
        for x in range(width):
            if current is not None and (x, y) == current:
                row += "X"
            elif inside and (x, y) in ins:
                row += "I"
            elif (x, y) in seen:
                row += box.get(tiles[(x, y)], "S")
            else:
                row += "."
        print(row)


printmaze(inside=True)
