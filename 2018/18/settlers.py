"""Module for Day 18: Settlers of The North Pole.
Part 1 is decent, but could be refactored.
Part 2 is hacky and needs human interpretation, but works.

"""
example = "\n".join(
    [
        ".#.#...|#.",
        ".....#|##|",
        ".|..|...#.",
        "..|#.....#",
        "#.#|||#|#|",
        "...#.||...",
        ".|....|...",
        "||...#|.#|",
        "|.||||..|.",
        "...#.|..|.",
    ]
)

main_input = "\n".join(
    [
        "#||.|...#.......#|#|....#.|#.#.|...#.|#........##.",
        "...#...##.#...##|.....|..|....|......#||..#.|.##.#",
        "..||..####|||.||#|....##|#.##|.#...##.|.|.||.#.##|",
        ".||#..||.||..|||...|.....##..#..........||.#..#...",
        "|...|...|.....#......||#|..|.....##.||.#..##|.#||#",
        "|...#.|.||#|#..|..|..#|#|.##.....|...#|.#....#..#.",
        "|...#...#|#.|#.#||....#..||.|..|.||.|.|.....#..|#|",
        "..|..##..#..|###.||...|||#.#...#.#....##...|..|..|",
        "..##...#.......#|#|#...#..##.#........|.|#......|.",
        "|..|#..|##|...#....#.##|...#.....|...........|#..|",
        "|....|.|#..##|.|##||.#.....|.#..#|.#.#|#|.......#|",
        "||..#.##..##...#|#.#...#|.##..###.....#..#.|..|##|",
        "#|#|..|.#.|.#.|.|...||#.|..#....#..|...||..|..#|.#",
        ".###..|....|.#||#..##.#|..|||..##|.||....|.#.|....",
        "|....#..#####......|||||##..|...#........#..|...##",
        "..##........|...||......##.#.#...|..|#...#|....|..",
        "||...#.#|..#||.....|#.#.|.....|.|..#.#.|....#.#..|",
        "......#..##.|.#|..|||#.........|#.|#|.|...|.|#..#.",
        "||...#..##|..|#.#|.....#.|...|.|...|.|.|..#.#..#.|",
        "....#...#..###||.||.##....#....||..|...||.|..|...#",
        ".#..#.#|....|.#.|#|.....#|.......||..##...#..#|.|.",
        "......#||##..#...#..|..#.|....||...#...|.#...#.#.|",
        "....||.....|.|#..||.#||....#..#.|.#...||.|.|....#.",
        "#.|.#.#..|.....|||.......#.#.#.|.#......#....||#.|",
        "|....##......|.||#.|...#.#...#|...|.||..|.#..|....",
        "||##..#......#|.#|.||||#.#...#.#.###.|#..#####....",
        "#.|..|#|#....#.|..||#|###|..|.|...|.#..|.|.#..##||",
        "..#..#..#...|..#.|....|||..#||.|.....|..#......||.",
        "||....||..|#||....|..#.##..|||#|.#|.#.||.||..||...",
        ".|.|.|##..|.##..|....#.#.#||....#...#|.#....##.#.|",
        "|.#....|.#...#..#...|.#.|#...|||..|#.#...|...#...|",
        "..|##...#..#.....|.|.#....#....||.#.|.#......|||##",
        "...||#...#|#........#..#.|.#...|||.......###..#...",
        "#.|.|#.#..#...#.....#..#....|.|..#...#.###.....#|#",
        "#...|.#..|.|||..||...##..|.....|##...||....###.##.",
        "##|.#..##..|.|.#.#.|#..##...|..|.#.||#..|...#|..##",
        ".#...#....##....||.#.|.|.|..|.|.###......#.###.|.#",
        "|.|.#..|#.#|..#.#...|.#|||#.#.....#.|#|||..#..|#..",
        "...|#...||#.#.|....|......|..#|.|.......#.##..##..",
        "..#....|.#.|....#|##...#||##......|#.|..|.|..#.|..",
        "||.|.#|.|#|#.......|.|#...|.#...|#..|....###..#.##",
        "..|.#|...|.#.#.#.#.#|..#...#..#|...#...#.......#..",
        "##|.....||#...#...|...|#...#.#......||..........|#",
        "..##.##....#.|.##..|#....|#...#|....#.##|.|#.||...",
        ".|....#...|...#..|##.###|#.#..|...||||.#.#.|.#....",
        "|..#|....|...#.....|..#|..||.|......#..||...#|.|.|",
        "|...#.#||..#..||.....|.....#|||...|...#|..|#.#|#.#",
        ".|.........#..|###......||.|#|..||#.|..|.|.....|.#",
        "||#..|..|.||#|.#|##|...#.##..#||.|....##....|.#||.",
        ".#....|#.#....|.|.|#..#......|||...#....|.........",
    ]
)

NEIGHBOURS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def create_acres(string):
    return [list(row) for row in string.split("\n")]


def is_valid(acres, i, j):
    return 0 <= i < len(acres[0]) and 0 <= j < len(acres)


def is_tree(acres, i, j):
    return acres[i][j] == "|"


def is_lumberyard(acres, i, j):
    return acres[i][j] == "#"


def has_3_or_more_trees(acres, i, j):
    counts = sum(
        1
        for x, y in NEIGHBOURS
        if is_valid(acres, x + i, y + j) and is_tree(acres, x + i, y + j)
    )
    return counts >= 3


def has_3_or_more_lumberyards(acres, i, j):
    counts = sum(
        1
        for x, y in NEIGHBOURS
        if is_valid(acres, x + i, y + j) and is_lumberyard(acres, x + i, y + j)
    )
    return counts >= 3


def has_least_one_lumberyard_and_tree(acres, i, j):
    lumber_counts = sum(
        1
        for x, y in NEIGHBOURS
        if is_valid(acres, x + i, y + j) and is_lumberyard(acres, x + i, y + j)
    )
    tree_counts = sum(
        1
        for x, y in NEIGHBOURS
        if is_valid(acres, x + i, y + j) and is_tree(acres, x + i, y + j)
    )
    return lumber_counts >= 1 and tree_counts >= 1


def pprint_acres(acres):
    for row in acres:
        print("".join(row))


def run(acres):
    width = len(acres[0])
    height = len(acres)

    new_acres = [["o"] * height for __ in range(width)]

    for i in range(width):
        for j in range(height):
            if acres[i][j] == "." and has_3_or_more_trees(acres, i, j):
                new_acres[i][j] = "|"
            elif acres[i][j] == "|" and has_3_or_more_lumberyards(acres, i, j):
                new_acres[i][j] = "#"
            elif acres[i][j] == "#" and not has_least_one_lumberyard_and_tree(
                acres, i, j
            ):
                new_acres[i][j] = "."
            else:
                new_acres[i][j] = acres[i][j]
    return new_acres


acres = create_acres(main_input)
counts = []
recurrent = {}
for i in range(1000):
    acres = run(acres)
    pprint_acres(acres)
    lumber_counts = sum(
        1
        for i in range(len(acres[0]))
        for j in range(len(acres))
        if is_lumberyard(acres, i, j)
    )
    tree_counts = sum(
        1 for i in range(len(acres[0])) for j in range(len(acres)) if is_tree(acres, i, j)
    )
    resource_value = lumber_counts * tree_counts
    if resource_value in counts:
        if not resource_value in recurrent:
            recurrent[resource_value] = [i]
        else:
            recurrent[resource_value].append(i)
        print("I'VE SEEN THIS BEFORE!!!!", resource_value)
    else:
        counts.append(resource_value)
    print()

print(recurrent)
firsts = []
for k, v in recurrent.items():
    if len(v) > 1:
        diffs = []
        for i in range(1, len(v)):
            diffs.append(v[i]-v[i-1])
        print(v[0], diffs)
        firsts.append(v[0] + 1)
time = 1000000000

for f in firsts:
    res = (time - f)/28
    print(res)
    if res == int(res):
        print("\t\tHERE!!!!", f - 1)
# Then I manually look up the corresponding resource_value for output f - 1
