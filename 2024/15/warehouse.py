""" Advent of Code 2024. Day 15: Warehouse Woes """

testinput = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".split(
    "\n\n"
)
testinput = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".split(
    "\n\n"
)

# testinput = """#######
##...#.#
##.....#
##..OO@#
##..O..#
##.....#
########
#
# <vv<<^^<<^^
# """.split(
#    "\n\n"
# )

with open("input.txt") as f:
    testinput = f.read().split("\n\n")


rawmap, moves = testinput
rawmap = rawmap.splitlines()


def parse_map(txtmap):
    walls = set()
    boxes = set()

    for i, line in enumerate(txtmap):
        for j, cell in enumerate(line):
            if cell == "#":
                walls.add((i, j))
            elif cell == "O":
                boxes.add((i, j))
            elif cell == "@":
                robot = (i, j)

    return robot, walls, boxes


robot, walls, boxes = parse_map(rawmap)


def move(d, robot, boxes):
    di, dj = d
    i, j = robot

    # If blank space, no issue, just move
    if (i + di, j + dj) not in boxes | walls:
        return (i + di, j + dj), boxes

    # If wall, can't move, no question
    if (i + di, j + dj) in walls:
        return robot, boxes

    # If box, investigation needed
    n = 1
    while (i + n * di, j + n * dj) in boxes:
        n += 1

        # If blank space, no issue, just move, but boxes need update
        if (i + n * di, j + n * dj) not in boxes | walls:
            for m in range(1, n):
                # Temporary remove all affected boxes
                boxes.remove((i + m * di, j + m * dj))
            for m in range(1, n):
                # Then add them back
                boxes.add((i + (m + 1) * di, j + (m + 1) * dj))

            return (i + di, j + dj), boxes

        # If wall, can't move, no question
        if (i + n * di, j + n * dj) in walls:
            return robot, boxes


def pprint(robot, boxes, part=1, rightboxes=None):
    if rightboxes is None:
        rightboxes = []
    for i in range(len(rawmap)):
        line = ""
        for j in range(part * len(rawmap[0])):
            if (i, j) in walls:
                line += "#"
            elif (i, j) in boxes:
                if part == 1:
                    line += "O"
                elif part == 2:
                    line += "["
            elif (i, j) in rightboxes:
                line += "]"
            elif (i, j) == robot:
                line += "@"
            else:
                line += "."
        print(line)


def boxmove(i, j, di, dj, boxes=None):
    if boxes is None:
        boxes = set()
    # Check if box at i, j can be moved in direction di, dj
    # If blank space, no issue, just move
    if (i + di, j + dj) not in leftboxes | rightboxes | walls:
        return True, boxes

    # If wall, can't move, no question
    if (i + di, j + dj) in walls:
        return False, boxes

    # If box, investigation needed
    # ALL boxes above or below must be movable
    boxes.add((i + di, j + dj))
    return boxmove(i + di, j + dj, di, dj, boxes)


dirs = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

for m in moves:
    if m == "\n":
        continue
    robot, boxes = move(dirs[m], robot, boxes)
pprint(robot, boxes)


def gps(boxes):
    return sum(100 * i + j for i, j in boxes)


print("Part 1:\t", gps(boxes))


def parse_map(txtmap):
    walls = set()
    leftboxes = set()
    rightboxes = set()

    for i, line in enumerate(txtmap):
        for j, cell in enumerate(line):
            if cell == "#":
                walls.add((i, 2 * j))
                walls.add((i, 2 * j + 1))
            elif cell == "O":
                leftboxes.add((i, 2 * j))
                rightboxes.add((i, 2 * j + 1))
            elif cell == "@":
                robot = (i, 2 * j)

    return robot, walls, leftboxes, rightboxes


robot, walls, leftboxes, rightboxes = parse_map(rawmap)
# pprint(robot, leftboxes, part=2, rightboxes=rightboxes)


def move(
    d,
    robot,
    leftboxes,
    rightboxes,
):
    di, dj = d
    i, j = robot

    can_move, boxes = boxmove(i, j, di, dj)

    if not can_move:
        return robot, set()

    # Check if these boxes have movable halves
    queue = list(boxes)
    visited = set()
    while queue:
        k, l = queue.pop()
        if (k, l) in visited:
            continue

        visited.add((k, l))

        if (k, l) in leftboxes:
            can_move, newboxes = boxmove(k - di, l + 1, di, dj)
            if not can_move:
                return robot, set()
            if can_move and (k, l + 1) in rightboxes:
                queue.append((k, l + 1))
        if (k, l) in rightboxes:
            can_move, newboxes = boxmove(k - di, l - 1, di, dj)
            if not can_move:
                return robot, set()
            if can_move and (k, l - 1) in leftboxes:
                queue.append((k, l - 1))

        queue.extend(list(newboxes))

        boxes.update(newboxes)

    return (i + di, j + dj), boxes


for m in moves:
    if m == "\n":
        continue

    robot, boxes = move(dirs[m], robot, leftboxes, rightboxes)
    # Move boxes
    leftremove = {b for b in boxes if b in leftboxes}
    rightremove = boxes - leftremove

    # Remove boxes
    leftboxes -= leftremove
    rightboxes -= rightremove

    di, dj = dirs[m]
    for k, l in leftremove:
        # Then add them back
        leftboxes.add((k + di, l + dj))
    for k, l in rightremove:
        # Then add them back
        rightboxes.add((k + di, l + dj))
    # pprint(robot, leftboxes, part=2, rightboxes=rightboxes)
    # input()

# pprint(robot, leftboxes, part=2, rightboxes=rightboxes)


def gps(boxes):
    return sum(100 * i + j for i, j in boxes)


print("Part 2:\t", gps(leftboxes))
