""" Advent of Code 2016. Day 13: A Maze of Twisty Little Cubicles """
NUMBER = 10
X, Y = 7, 4

def is_wall(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y
    n += NUMBER
    b = bin(n).count("1")
    return b % 2


dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = [(1, 1, 0)]
visited = set()

while queue:
    x, y, steps = queue.pop(0)
    visited.add((x, y))

    if x == X and y == Y:
        print("Part 1:\t", steps)
        break

    if steps == 50:
        print("Part 2:\t", len(visited))

    for dx, dy in dirs: 
        if x + dx < 0 or y + dy < 0:
            continue
        if (x+dx, y+dy) in visited:
            continue
        if is_wall(x+dx, y+dy):
            continue

        queue.append((x+dx, y+dy, steps + 1))

