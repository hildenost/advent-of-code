""" Advent of Code 2016. Day 19: An Elephant Named Joseph """

elves = [i+1 for i in range(n_elves)]
while len(elves) > 1:
    modulo = len(elves) % 2
    elves = elves[::2]
    if modulo:
        # The last elf will steal from the first
        elves = elves[1:]
print("Part 1:\t", elves[0])

### PART 2
import math
elves = [i+1 for i in range(n_elves)]
while len(elves) > 1:
    modulo = len(elves) % 3

    if modulo == 0: 
        # keep every third elf
        # example 9 elves
        # 1 2 3 4 5 6 7 8 9
        # x x 3 x x 6 x x 9
        elves = elves[2::3]
        continue
    
    # Else we need to divide the elves group in roughly half 
    n = math.ceil(len(elves)/2) if len(elves) % 2 else len(elves) // 2 - 1

    # The latter half keeps every third elf starting with the first
    # The former half keeps every third elf starting with 
    # alternating first or second elf depending on the modulo 3
    elves = elves[:n][modulo-1::3] + elves[n:][::3]

print("Part 2:\t", elves[0])


