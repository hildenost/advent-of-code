""" Advent of Code 2024. Day 18: RAM Run """

byteposes = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".splitlines()

with open("input.txt") as f:
    byteposes = f.read().splitlines()

byteposes = [tuple(int(n) for n in l.split(",")) for l in byteposes]


def pprint(path, nbytes=12):
    for i in range(ymax):
        line = ""
        for j in range(xmax):
            if (j, i) in byteposes[:12]:
                line += "#"
            elif (j, i) in path:
                line += "O"
            else:
                line += "."
        print(line)


xmax = ymax = 70
N = 1024

start = (0, 0)
end = (xmax, ymax)


def is_within_bounds(x, y):
    return 0 <= x <= xmax and 0 <= y <= ymax


def neighbours(x, y):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return [(x + dx, y + dy) for dx, dy in dirs]


from collections import namedtuple

Node = namedtuple("Node", "x y cost")


def dijkstra(start, end, b=1024):
    walls = byteposes[:b]

    visited = dict()

    startnode = Node(*start, 0)

    queue = [startnode]

    visited[(startnode.x, startnode.y)] = 0

    while queue:
        n = queue.pop(0)
        # print(n, visited)

        for x, y in neighbours(n.x, n.y):
            if not is_within_bounds(x, y):
                continue

            if (x, y) in walls:
                continue

            new_cost = n.cost + 1

            if (x, y) in visited and new_cost >= visited[(x, y)]:
                # Been here
                continue

            visited[(x, y)] = new_cost

            new_node = Node(x, y, new_cost)
            queue.append(new_node)
    return visited.get(end)


best = dijkstra(start, end, b=N)
print("Part 1:\t", best)

nmax = len(byteposes)

reachable = {N: True}

left = N
right = nmax

while left <= right:
    m = (left + right) // 2

    test = dijkstra(start, end, b=m)

    if test is not None:
        # We have a reachable path
        reachable[m] = True
        # Moving right
        left = m + 1
    else:
        # We don't have a reachable path
        reachable[m] = False
        # Checking if the neighbour to the left is True
        # Because if it is, we've found the answer
        if reachable.get(m - 1, False):
            break
        # Moving left
        right = m - 1
print("Part 2:\t", byteposes[m - 1])
