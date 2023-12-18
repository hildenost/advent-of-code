""" Advent of Code 2023. Day 18: Lavaduct Lagoon """


with open("input.txt") as f:
    digplan = [row.split() for row in f.read().splitlines()]

dirs = {
    "U": lambda x, y, s: (x, y - s),
    "D": lambda x, y, s: (x, y + s),
    "L": lambda x, y, s: (x - s, y),
    "R": lambda x, y, s: (x + s, y),
}


def solve(part=1):
    head = (0, 0)

    vertices = [head]
    circumference = 0
    for direction, steps, number in digplan:
        if part == 2:
            direction, steps = hextranslate(number)

        head = dirs[direction](*head, int(steps))

        circumference += int(steps)

        vertices.append(head)

    A = area(vertices)

    # No idea why this works, but it does
    return A + circumference // 2 + 1


def signed_area(a, b):
    # Shoelace formula
    return a[0] * b[1] - b[0] * a[1]


def area(vertices):
    total_area = sum(signed_area(p1, p2) for p1, p2 in zip(vertices, vertices[1:]))
    return total_area // 2


encoded_dirs = {str(i): d for i, d in enumerate("RDLU")}


def hextranslate(number):
    # The hex is on the form (#DDDDDD)
    distance = number[2:7]
    direction = number[-2]
    return encoded_dirs[direction], int(distance, 16)


print("Part 1:\t", solve())
print("Part 2:\t", solve(part=2))


def slow_flood_fill(start, dug):
    # Inefficient flood fill ahead
    # Or how I got that first star
    queue = [start]
    filled = {start}

    while queue:
        x, y = queue.pop()

        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            if (x + dx, y + dy) in dug | filled:
                continue

            queue.append((x + dx, y + dy))
            filled.add((x + dx, y + dy))
    return len(filled | dug)


# Starting point found by manual inspection
# And dug is a set of the entire circumference
# print("Part 1:\t", slow_flood_fill(start, dug))
