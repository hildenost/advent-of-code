""" Advent of Code 2016. Day 22: Grid Computing """
import re

pattern = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)\s+\w+\s+(\d+)T\s+(\d+)T")

with open("input.txt") as f:
    __, __, *df = f.read().splitlines()

df = """/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%
""".splitlines()

# Initialize grid
grid = {}
for line in df:
    x, y, used, avail = [int(g) for g in re.search(pattern, line).groups()]
    grid[(x, y)] = [used, avail]


SIZE = 30
SIZE, __ = max(grid.keys())
all_nodes = [(x, y) for x in range(SIZE + 1) for y in range(SIZE + 1)]


# viable_pairs = sum(
#    grid[A][0] <= grid[B][1]
#    for A in all_nodes
#    for B in all_nodes
#    if grid[A][0] > 0 and A != B
# )
#
# print("Part 1:\t", viable_pairs)
print("GOAL data:\t", grid[(SIZE, 0)])

# Keeping the size of the goal data
G = grid[(SIZE, 0)][0]
goal = (0, 0)
queue = [(0, SIZE, 0, grid)]

# The spots where G has been
neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def movearound(start, g):
    print()
    print("Inside subqueue")
    # This should be recursive also?
    steps = {key: 99999999999999999999999999999999999999 for key in all_nodes}
    steps[start] = 0
    # End criteria:
    # - Can move
    # - Cannot move at all
    G = g[start][0]
    visited = set()
    queue = [(0, *start, g)]
    while queue:
        queue.sort()
        __, x, y, g = queue.pop(0)

        print(visited)
        if (x, y) in visited:
            continue
        print()
        print()
        print("WE AT ", x, y, " with data: ", g[(x, y)])
        for dx, dy in neighbours:
            print()
            if (x + dx, y + dy) in grid:
                print("WANNA VISIT ", x + dx, y + dy)
                print("Can we move to ", x + dx, y + dy, " right away?")
                print("Goal size: ", G, "\t available at target: ", g[(x + dx, y + dy)])
                print(steps[(x + dx, y + dy)], steps[(x, y)])
                if G <= g[(x + dx, y + dy)][1]:
                    print("MOVING AT ONCE!!!")
                    print("only one move")
                    new_g = g.copy()
                    # used
                    new_g[(x + dx, y + dy)][0] += G
                    # avail
                    new_g[(x + dx, y + dy)][1] -= G
                    # old spot
                    new_g[(x, y)][0] -= G
                    new_g[(x, y)][1] += G
                    print(new_g[(x, y)])
                    print(new_g[(x + dx, y + dy)])
                    steps[(x + dx, y + dy)] = min(
                        steps[(x + dx, y + dy)], steps[(x, y)] + 1
                    )
                    print(steps[(x + dx, y + dy)], steps[(x, y)])
                    return (steps[(x + dx, y + dy)], new_g)
                elif G <= sum(g[(x + dx, y + dy)]):
                    print("GOT SPACE, but must move around stuffs first")
                    # time to recurse?
                    steps[(x + dx, y + dy)] = min(
                        steps[(x + dx, y + dy)], steps[(x, y)] + 1
                    )
                    print(steps[(x + dx, y + dy)], steps[(x, y)])
                    queue.append((steps[(x + dx, y + dy)], x + dx, y + dy, g.copy()))
        visited.add((x, y))
    print("Nope, cannot")
    return


# This should be recursive also?
steps = {key: 99999999999999999999999999999999999999 for key in all_nodes}
steps[(SIZE, 0)] = 0


def move(start, end, g):

    G = g[start][0]
    visited = set()
    queue = [(0, *start, g)]
    while queue:
        queue.sort()
        __, x, y, g = queue.pop(0)

        if (x, y) == end:
            print("DONE")
            return

        if (x, y) in visited:
            continue
        print()
        print()
        print("WE AT ", x, y, " with data: ", g[(x, y)])
        for dx, dy in neighbours:
            print()
            if (x + dx, y + dy) in grid:
                print("WANNA VISIT ", x + dx, y + dy)
                print("Can we move to ", x + dx, y + dy, " right away?")
                print("Goal size: ", G, "\t available at target: ", g[(x + dx, y + dy)])
                print(steps[(x + dx, y + dy)])
                if G <= g[(x + dx, y + dy)][1]:
                    print("MOVING AT ONCE!!!")
                    print("only one move")
                    new_g = g.copy()
                    # used
                    new_g[(x + dx, y + dy)][0] += G
                    # avail
                    new_g[(x + dx, y + dy)][1] -= G
                    # old spot
                    new_g[(x, y)][0] -= G
                    new_g[(x, y)][0] += G
                    print(new_g[(x, y)])
                    print(new_g[(x + dx, y + dy)])
                    steps[(x + dx, y + dy)] = min(
                        steps[(x + dx, y + dy)], steps[(x, y)] + 1
                    )
                    queue.append((steps[(x + dx, y + dy)], x + dx, y + dy, new_g))
                elif G <= sum(g[(x + dx, y + dy)]):
                    s, new_g = movearound((x + dx, y + dy), g.copy())
                    print("WE HAVE MOVED AROUND")
                    steps[(x + dx, y + dy)] = min(
                        steps[(x + dx, y + dy)], steps[(x, y)] + s
                    )
                    print(steps[(x + dx, y + dy)], steps[(x, y)], s)
                    queue.append((steps[(x + dx, y + dy)], x + dx, y + dy, new_g))
                else:
                    print("CANNOT GO HERE :( :( :(")
        visited.add((x, y))
    print("Nope, cannot")
    return


print(move((SIZE, 0), (0, 0), grid))

print(steps)
exit()

x, y = (0, 0)
d[y][x] = 0
queue = [(0, x, y)]
while queue:
    queue.sort()
    __, x, y = queue.pop(0)
    if (x, y) in visited:
        continue

    for dx, dy in neighbours:
        fx = (x + dx) // len(cave[0])
        fy = (y + dy) // len(cave)
        if 0 <= fx < 5 and 0 <= fy < 5:
            d[y + dy][x + dx] = min(
                d[y][x] + get_value(x + dx, y + dy, fx, fy), d[y + dy][x + dx]
            )
            queue.append((d[y + dy][x + dx], x + dx, y + dy))

    visited.add((x, y))
