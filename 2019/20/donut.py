def print_maze(maze, seen, queue, curr, level=0):
    for y, line in enumerate(maze):
        print(''.join(
            "$" if ((x, y), level) == curr else
            "O" if ((x, y), level) in queue else
            "X" if ((x, y), level) in seen else c
            for x, c in enumerate(line)))
    print()
    print(f"\t\t LEVEL {level}")

def get_portal_name(a, b):
    return ''.join(sorted(a+b))

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

with open("input.txt", "r") as f:
    input_maze = f.read().splitlines()

portals, start_node = find_portals(input_maze)

def divide_portals(maze, portals):
    # Need to find out which of the portals are on the outside
    width = len(maze[0])
    height = len(maze)

    outer = {}
    inner = {}
    for x, y in portals:
        if 5 <= x <= width - 5 and 5 <= y <= height - 5: 
            inner[portals[(x, y)]] = (x, y)
        else:
            outer[portals[(x, y)]] = (x, y)
    return outer, inner


def bfs(maze, start_node, portals, part=1):
    queue = [(start_node, 0)]
    seen = {(start_node, 0)}
    cost = {}
    cost[(start_node, 0)] = 0

    outer, inner = divide_portals(maze, portals) 

    while queue:
        (x, y), level = queue.pop(0)

        prev_cost = cost[((x, y), level)]

        if (x, y) in portals:
            # It costs an extra step to warp
            prev_cost += 1

            name = portals[(x, y)]

            # Finally found the exit at the right level!
            if name == "ZZ" and level == 0:
                return cost[((x, y), level)]
            elif name == "ZZ":
                # This is a dead end
                continue

            is_outer = outer[name] == (x, y)

            if is_outer and level == 0:
                # We at outermost layer, but not at exit 
                # Aborting branch
                continue

            # Warping
            x, y = inner[name] if is_outer else outer[name]

            if part == 2:
                # Adjusting recursion levels
                level += (-1) if is_outer else 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            node = (x+dx, y+dy)
            if maze[y+dy][x+dx] == "." and (node, level) not in seen:
                cost[(node, level)] = prev_cost + 1
                seen.add((node, level))
                queue.append((node, level))

print("Part 1:\t", bfs(input_maze, start_node, portals))
print("Part 2:\t", bfs(input_maze, start_node, portals, part=2))
