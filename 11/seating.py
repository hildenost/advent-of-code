""" Advent of Code 2020 Day 11: Seating System """
from collections import defaultdict

test = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

test = """\
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
"""

test = """\
.............
.L.L.#.#.#.#.
.............
"""

test = """\
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
"""


seats = [list(l) for l in test.splitlines()]


with open("11/input.txt") as f:
    seats = [list(l) for l in f.read().splitlines()]

DIRECTIONS = {(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}


def pprint(matrise):
    for rad in matrise:
        print("".join(rad).replace("F", "."))
    print()


def within_bounds(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def count_neighbours(i, j, matrix):
    return sum(
        matrix[i + y][j + x] == "#"
        for y, x in DIRECTIONS
        if within_bounds(i + y, j + x, matrix)
    )


def count_visible_seats(i, j, matrix):
    visible = 0
    for y, x in DIRECTIONS:
        n = 1
        while within_bounds(i + n * y, j + n * x, matrix):
            if matrix[i + n * y][j + n * x] == "#":
                visible += 1
                break
            elif matrix[i + n * y][j + n * x] == "L":
                break
            n += 1
    return visible


def get_changed_seats(matrix):
    changed_seats = defaultdict(str)
    for i, row in enumerate(matrix):
        for j, seat in enumerate(row):
            if seat != ".":
                n = count_neighbours(i, j, matrix)
                if seat == "L" and n == 0:
                    changed_seats[(i, j)] = "#"
                elif seat == "#" and n >= 4:
                    changed_seats[(i, j)] = "L"
    return changed_seats


def get_changed_seats_2(matrix):
    changed_seats = defaultdict(str)
    for i, row in enumerate(matrix):
        for j, seat in enumerate(row):
            if seat != ".":
                n = count_visible_seats(i, j, matrix)
                if seat == "L" and n == 0:
                    changed_seats[(i, j)] = "#"
                elif seat == "#" and n >= 5:
                    changed_seats[(i, j)] = "L"
    return changed_seats


def count_occupied(matrix):
    return sum(sum(seat == "#" for seat in row) for row in matrix)


# pprint(seats)
while True:
    changed_states = get_changed_seats_2(seats)
    if not changed_states:
        break
    for (i, j), state in changed_states.items():
        seats[i][j] = state
    # pprint(seats)

print(count_occupied(seats))
