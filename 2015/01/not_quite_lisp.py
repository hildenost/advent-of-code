""" Advent of Code 2015 Day 1: Not Quite Lisp """

with open("01/input.txt") as f:
    directions = f.read()

### PART 1
# ( meant up one floor
# ) meant down one floor
# The final floor will just be the number of ups minus the number of downs
print(directions.count("(") - directions.count(")"))

### PART 2
# Just traversing the directions, quitting the loop when floor drops below 0
floor = 0
for i, d in enumerate(directions):
    floor += 1 if d == "(" else -1

    if floor < 0:
        print(i + 1)
        break

