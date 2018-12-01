"""Advent of code 2018: 2/2 on 1 Dec

Finding and printing first repeated frequency.

"""

with open("input.txt") as f:
    lines = f.readlines()
    sums = [0]
    found = False
    while not found:
        for line in lines:
            s = int(line) + sums[-1]
            if s in sums:
                print("First repeated frequency:\t", s)
                found = True
                break
            else:
                sums.append(s)
