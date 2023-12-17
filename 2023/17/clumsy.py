""" Advent of Code 2023. Day 17: Clumsy Crucible """

with open("input.txt") as f:
    heatmap = f.read().splitlines()

heatmap = [[int(n) for n in row] for row in heatmap]
width, height = len(heatmap[0]), len(heatmap)

from heapq import heappush
from heapq import heappop


def neighbours(x, y, direction):
    if direction == ">":
        return [(x + 1, y, direction), (x, y + 1, "v"), (x, y - 1, "^")]
    if direction == "<":
        return [(x - 1, y, direction), (x, y + 1, "v"), (x, y - 1, "^")]
    if direction == "^":
        return [(x + 1, y, ">"), (x - 1, y, "<"), (x, y - 1, "^")]
    if direction == "v":
        return [(x + 1, y, ">"), (x - 1, y, "<"), (x, y + 1, "v")]


def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# node = (priority, cost, x, y, direction, consecutive dirs)
goal = (width - 1, height - 1)
h = heuristic(0, 0, *goal)
node = (h, 0, 0, 0, ">", 0)
node_2 = (h, 0, 0, 0, "v", 0)


queue = [node, node_2]

seen = set()

while queue:
    h, c, *pos, count_dirs = heappop(queue)
    pos = tuple(pos)
    if (pos, count_dirs) in seen:
        continue

    seen.add((pos, count_dirs))
    # print(h, c, pos, count_dirs, len(seen))
    if goal[0] == pos[0] and goal[1] == pos[1]:
        print("Part 1:\t", h)
        break
    for x, y, direction in neighbours(*pos):
        if 0 <= x < width and 0 <= y < height:
            # print(x, y, direction)
            # print(heatmap[y][x])
            if direction == pos[-1]:
                # Same direction
                if count_dirs == 2:
                    # Illegal, must turn
                    continue

                consecutive = count_dirs + 1

            else:
                consecutive = 0

            new_cost = c + heatmap[y][x]
            h = heuristic(x, y, *goal)

            new_node = (new_cost + h, new_cost, x, y, direction, consecutive)
            if ((x, y, direction), consecutive) not in seen:
                heappush(queue, new_node)


########## PART 2

goal = (width - 1, height - 1)
h = heuristic(0, 0, *goal)
node = (h, 0, 0, 0, ">", 1)
node_2 = (h, 0, 0, 0, "v", 1)

max_consecutive = 10
min_consecutive = 4

queue = [node, node_2]

seen = set()

while queue:
    h, c, *pos, count_dirs = heappop(queue)
    pos = tuple(pos)
    if (pos, count_dirs) in seen:
        continue

    seen.add((pos, count_dirs))
    # print(h, c, pos, count_dirs, len(seen))
    if goal[0] == pos[0] and goal[1] == pos[1] and count_dirs >= min_consecutive:
        print("Part 2:\t", h)
        break
    for x, y, direction in neighbours(*pos):
        if 0 <= x < width and 0 <= y < height:
            # print(x, y, direction)
            # print(heatmap[y][x])
            if direction == pos[-1]:
                # Same direction
                if count_dirs == max_consecutive:
                    # Illegal, must turn
                    continue

                consecutive = count_dirs + 1

            else:
                # Different direction
                # Cannot turn if consequent is less than the demand
                if count_dirs < min_consecutive:
                    continue

                consecutive = 1

            new_cost = c + heatmap[y][x]
            h = heuristic(x, y, *goal)

            new_node = (new_cost + h, new_cost, x, y, direction, consecutive)
            if ((x, y, direction), consecutive) not in seen:
                heappush(queue, new_node)
