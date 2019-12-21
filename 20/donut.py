from collections import defaultdict

example = [
    "         A          ",
    "         A          ",
    "  #######.######### ",
    "  #######.........# ",
    "  #######.#######.# ",
    "  #######.#######.# ",
    "  #######.#######.# ",
    "  #####  B    ###.# ",
    "BC...##  C    ###.# ",
    "  ##.##       ###.# ",
    "  ##...DE  F  ###.# ",
    "  #####    G  ###.# ",
    "  #########.#####.# ",
    "DE..#######...###.# ",
    "  #.#########.###.# ",
    "FG..#########.....# ",
    "  ###########.##### ",
    "             Z      ",
    "             Z      ",
]
larger_example = [
    "                   A               ",
    "                   A               ",
    "  #################.#############  ",
    "  #.#...#...................#.#.#  ",
    "  #.#.#.###.###.###.#########.#.#  ",
    "  #.#.#.......#...#.....#.#.#...#  ",
    "  #.#########.###.#####.#.#.###.#  ",
    "  #.............#.#.....#.......#  ",
    "  ###.###########.###.#####.#.#.#  ",
    "  #.....#        A   C    #.#.#.#  ",
    "  #######        S   P    #####.#  ",
    "  #.#...#                 #......VT",
    "  #.#.#.#                 #.#####  ",
    "  #...#.#               YN....#.#  ",
    "  #.###.#                 #####.#  ",
    "DI....#.#                 #.....#  ",
    "  #####.#                 #.###.#  ",
    "ZZ......#               QG....#..AS",
    "  ###.###                 #######  ",
    "JO..#.#.#                 #.....#  ",
    "  #.#.#.#                 ###.#.#  ",
    "  #...#..DI             BU....#..LF",
    "  #####.#                 #.#####  ",
    "YN......#               VT..#....QG",
    "  #.###.#                 #.###.#  ",
    "  #.#...#                 #.....#  ",
    "  ###.###    J L     J    #.#.###  ",
    "  #.....#    O F     P    #.#...#  ",
    "  #.###.#####.#.#####.#####.###.#  ",
    "  #...#.#.#...#.....#.....#.#...#  ",
    "  #.#####.###.###.#.#.#########.#  ",
    "  #...#.#.....#...#.#.#.#.....#.#  ",
    "  #.###.#####.###.###.#.#.#######  ",
    "  #.#.........#...#.............#  ",
    "  #########.###.###.#############  ",
    "           B   J   C               ",
    "           U   P   P               ",
]

def print_maze(maze, seen, queue, curr):
    for y, line in enumerate(maze):
        print(''.join(
            "$" if (x, y) == curr else
            "O" if (x, y) in queue else
            "X" if (x, y) in seen else c
            for x, c in enumerate(line)))

def get_portal_name(a, b):
    return ''.join(sorted(a+b))


def bfs(maze, start_node, portals):
    queue = [start_node]
    seen = {start_node}

    def valid_path(node, square):
        return (
            square == '.' and
            node not in seen and
            0 <= node[0] < len(maze[0]) and
            0 <= node[1] < len(maze)
        )

    def update_node(node):
        depths[node] = min(depths[(x, y)] + 1, depths[node])
        seen.add(node)
        queue.append(node)

    depths = defaultdict(lambda: 99999999999)
    depths[start_node] = 0

    while queue:
        x, y = queue.pop(0)
        #print_maze(maze, seen, queue, (x, y))

        if (x, y) in portals:
            name = portals[(x, y)]
            if name == "ZZ":
                return depths[(x, y)]

            del portals[(x, y)]
            node = [k for k, v in portals.items() if v == name][0]

            update_node(node)
            del portals[node]
        else:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                node = (x+dx, y+dy)
                if valid_path(node, maze[y+dy][x+dx]):
                    update_node(node)

def valid_range(x, y, maze):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze)

def find_portals(maze):
    squares = {(x, y)
               for x in range(len(maze[0]) - 1)
               for y in range(len(maze) - 1)
               if maze[y][x].isalpha()}
    portals = {}
    while squares:
        x, y = squares.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if valid_range(x+dx, y+dy, maze) and maze[y+dy][x+dx].isalpha():
                squares.discard((x+dx, y+dy))
                if valid_range(x+2*dx, y+2*dy, maze) and maze[y+2*dy][x+2*dx] == ".":
                    portal = (x+2*dx, y+2*dy)
                elif maze[y-dy][x-dx] == ".":
                    portal = (x-dx, y-dy)

                name = get_portal_name(maze[y][x], maze[y+dy][x+dx])
                if name == "AA":
                    start_node = portal
                else:
                    portals[portal] = name
    return portals, start_node


portals, start_node = find_portals(example)
assert 23 == bfs(example, start_node, portals)

portals, start_node = find_portals(larger_example)
assert 58 == bfs(larger_example, start_node, portals)

with open("input_maze.txt", "r") as f:
    input_maze = f.read().splitlines()

portals, start_node = find_portals(input_maze)
print(bfs(input_maze, start_node, portals))

