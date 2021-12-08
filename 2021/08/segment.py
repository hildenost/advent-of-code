""" Advent of Code 2021. Day 8: Seven Segment Search """
import re

with open("input.txt") as f:
    displays = f.read().splitlines()

counter = sum(
    len(d) in [2, 3, 4, 7] for display in displays for d in display.split()[-4:]
)
print("Part 1:\t", counter)

values = 0
for display in displays:
    # Unpacking the known numbers
    one, seven, four, *digits, eight = sorted(display.split()[:10], key=len)
    value = display.split()[-4:]

    out = [set() for __ in range(10)]

    # Finding the numbers
    # First the easy ones
    out[1] = set(one)  # the smallest length digit is 1
    out[7] = set(seven)  # the second smallest is 7
    out[4] = set(four)  # the third smallest is 4
    out[8] = set(eight)  # the largest is 8

    for d in digits:
        d = set(d)
        if out[4] < d:
            # the 9 shares ALL wires as number 4
            out[9] = d
        elif not out[1] < d and len(d) == 6:
            # the 6 will NOT have both wires as number 1
            out[6] = d
        elif out[1] < d and not out[4] < d and len(d) == 6:
            out[0] = d
        elif out[1] < d and len(d) == 5:
            # To separate 3 from 5 and 2
            # The 3 will have both wires as number 1
            out[3] = d
        elif len(out[4] & d) == 3 and not out[1] < d:
            # To separate 5 from 2
            # The 5 will share 3 out of 4 wires as number 4
            out[5] = d
        elif len(out[4] & d) == 2:
            out[2] = d

    values += int("".join(str(out.index(set(v))) for v in value))

print("Part 2:\t", values)

