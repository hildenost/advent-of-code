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

def increase(n, b):
    return tuple(c+1 if i in b else c for i, c in enumerate(n))


def astar(start, goal, buttons):
    # Need to track
    # number of button presses
    # and current state
    open_list = [(0, start)]
    closed_list = set()

    while open_list:
        (presses, n) = heappop(open_list)
        #print("At state ", n)
        #print("Goal state", goal)
        print(len(open_list))

        if n in closed_list:
            continue

        closed_list.add(n)

        if n == goal:
            return presses 

        for b in buttons:
            #print("Pressing button ", b)
            new = increase(n, b)
            #print("New state: ", new)
            # If any of the new state joltages are
            # more than goal, discard
            if not all(j <= g for j, g in zip(new, goal)):
                continue

            if new in closed_list:
                # Been at this state previously
                # Discard
                continue
            heappush(open_list, (presses + 1, new))
        #input()

def parse_button2(b):
    return tuple(int(n) for n in b.strip('()').split(','))

import numpy as np

def simplex(goal, buttons):
    print(goal)
    print(buttons)
    constraints = np.array(goal)
    Z = 0

    # Need the rows leading to the constraints
    rows = []
    for j, __ in enumerate(constraints):
        rows.append([int(j in b) for b in buttons])
    for row, c in zip(rows, constraints):
        print(row, "\t", c)

    rows = np.array(rows)


    # We are minimising just the sum of the
    # xis
    # We flip the sign

    # Maximise sum(-xi)
    # Subject to:
    # rows + identity(len(constraints)) + s_a = constraints
    # xi >= 0

    tableau = np.hstack((rows, np.identity(len(constraints), dtype=np.int32)))
    print(tableau)

    objective = np.hstack((
            np.array([1] * len(buttons)),
        np.array([0] * len(constraints))
    ))
    print(objective)


    print(constraints)
    print(constraints.argmin())

    # There exist several solutions
    # So should probably iterate through the various options
    # for the pivot column, row and entry

    print("HERE ARE THE CONSTRAINTS")
    print(constraints)
    is_feasible = all(constraints >= 0)
    print("BFS?\t", is_feasible)


    while (objective > 0).any():
        pivot_col = objective.argmax()
        print(pivot_col, objective[pivot_col])

        row_coeff = objective[pivot_col] - Z
        print(row_coeff)
        print(tableau[:, pivot_col])
        print(constraints)

        col = tableau[:, pivot_col]
        # Replacing the 0s with a small number
        a = np.where(col == 0, 0.2, col)
        print(a)
        print(constraints / a)
        pivot_row = (constraints/a).argmin()
        print(pivot_row)
        row = tableau[pivot_row]

        # If column already just 1 and rest 0, we skip
        if sum(c == 1 for c in col) > 1:
            print("ROW MAGIC")
            print(tableau)
            for k, row in enumerate(tableau):
                if k == pivot_row:
                    continue
                print(k, row, pivot_row, pivot_col)
                if row[pivot_col] == 0:
                    print("Already 0")
                else:
                    row -= tableau[pivot_row]
                    constraints[k] -= constraints[pivot_row]
            print(tableau)
            print(constraints)

        row = tableau[pivot_row]
        print("OK")
        print("Let's adjust the objective")
        print(row)
        print(objective)
        objective -= row
        print(objective)
        Z -= constraints[pivot_row]
        print(Z)


        print(constraints)
        print(np.array([[1, 2, 3, 4, 5, 6, -1]]))
        print(tableau)
        print(objective)
        #x1 = 7
        #x3 = 4 
        """
                  {0, 1, 2, 3}
        7 * (3) = {0, 0, 0, 7}
        4 * (2) = {0, 0, 4, 7}
        3 * (0,1)={3, 3, 4, 7}
        2 * (1, 3){3, 5, 4, 10}


        """

        input()



    pass

total_presses=0
for line in lines:
    __, *buttons, joltage = line
    c = parse_config(config)
    buttons = [
        parse_button2(b)
        for b in buttons]
    print(buttons)
    joltage = tuple(int(n) for n in joltage.strip('{}').split(','))
    print(joltage)

    start = tuple(0 for i in joltage)
    print(start)


    #presses = astar(start, joltage, buttons) 
    presses = simplex(joltage, buttons)
    total_presses += presses
    print(presses)

                
print("Part 1:\t", total_presses)

