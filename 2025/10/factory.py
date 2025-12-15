""" Advent of Code 2025. Day 10: Factory """

with open("input.txt") as f:
    lines = [row.split() for row in f.read().splitlines()]

example = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".splitlines()

lines = [row.split() for row in example]

def parse_config(config):
    return "".join("0" if i == "." else "1" for i in config.strip('[]'))

def parse_button(button, l):
    b = button.strip('()').split(",")

    return "".join(
        "0" if str(i) not in b else "1"
        for i in range(l)
    )

def toggle(config, button):
    return config ^ button


from heapq import heappush
from heapq import heappop

def astar(start, goal, buttons):
    # Need to track
    # number of button presses
    # and current state
    open_list = [(0, start)]
    closed_list = set()

    while open_list:
        (presses, n) = heappop(open_list)

        if n in closed_list:
            continue

        closed_list.add(n)

        if n == goal:
            return presses 

        for b in buttons:
            new = toggle(n, b)
            if new in closed_list:
                # Been at this state previously
                # Discard
                continue
            heappush(open_list, (presses + 1, new))


total_presses=0
for line in lines:
    config, *buttons, __ = line
    c = parse_config(config)
    buttons = [
        parse_button(b, len(c))
        for b in buttons]

    start = "0"*len(c)


    presses = astar(int(start, 2), int(c, 2), [int(b,2) for b in buttons])
    total_presses += presses

                
print("Part 1:\t", total_presses)

from scipy.optimize import linprog
import numpy as np


def parse_button2(b):
    return tuple(int(n) for n in b.strip("()").split(","))


total_presses = 0
for k, line in enumerate(lines):
    __, *buttons, joltage = line

    buttons = [parse_button2(b) for b in buttons]
    joltage = tuple(int(n) for n in joltage.strip("{}").split(","))

    tableau = np.array([[int(j in b) for b in buttons] for j in range(len(joltage))])
    c = np.array([1] * len(buttons))
    b_eq = np.array(joltage)

    # Ga opp å implementere Simplex selv
    res = linprog(c, A_eq=tableau, b_eq=b_eq, integrality=1)
    total_presses += res.fun

print("Part 2:\t", int(total_presses))
