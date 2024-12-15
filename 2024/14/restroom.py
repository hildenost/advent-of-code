""" Advent of Code 2024. Day 14: Restroom Redoubt """

testinput = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".splitlines()
xmax = 11
ymax = 7

with open("input.txt") as f:
    testinput = f.read().splitlines()
xmax = 101
ymax = 103


import re

robots = []
for line in testinput:
    numbers = [int(n) for n in re.findall("-?\d+", line)]
    pos, vel = numbers[:2], numbers[2:]
    robots.append((pos, vel))


def move(pos, vel):
    x, y = pos[0] + vel[0], pos[1] + vel[1]

    # check bounds
    if x >= xmax:
        # teleport
        x = x - xmax
    elif x < 0:
        # teleport
        x = xmax + x

    if y >= ymax:
        # teleport
        y = y - ymax
    elif y < 0:
        # teleport
        y = ymax + y

    return (x, y), vel


def find_quadrant(x, y):
    if 0 <= x < xmax // 2 and 0 <= y < ymax // 2:
        return 1

    if xmax // 2 + 1 <= x < xmax and 0 <= y < ymax // 2:
        return 2

    if 0 <= x < xmax // 2 and ymax // 2 + 1 <= y < ymax:
        return 3

    if xmax // 2 + 1 <= x < xmax and ymax // 2 + 1 <= y < ymax:
        return 4

    return 0


qs = [0, 0, 0, 0, 0]
for pos, vel in robots:
    for __ in range(100):
        pos, vel = move(pos, vel)
    qs[find_quadrant(*pos)] += 1

print("Part 1:\t", qs[1] * qs[2] * qs[3] * qs[4])


def pprint(poses):
    for y in range(ymax):
        line = ""
        for x in range(xmax):
            if (x, y) in poses:
                line += "X"
            else:
                line += " "
        print(line)


for t in range(50000):
    new_robots = []
    poses = set()
    for pos, vel in robots:
        pos, vel = move(pos, vel)
        new_robots.append((pos, vel))
        poses.add(pos)
    robots = new_robots

    # If no robots overlap, perhaps?
    if len(robots) == len(poses):
        pprint(poses)
        print("Part 2:\t", t + 1)
        break
