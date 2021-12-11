""" Advent of Code 2021. Day 11: Dumbo Octopus """
import numpy as np
from scipy.signal import convolve2d

octopuses = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".splitlines()

octopuses = np.array([[int(n) for n in row] for row in octopuses])

# Creating the rolling window
B = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]], dtype=int)

# Initialising the mask of flashing octopuses to all False
has_flashed = octopuses > 100

flashes = 0
step = 0
while not has_flashed.all():
    # First, increase all by one
    octopuses += 1

    # Check any flashes
    # Reset flash mask
    has_flashed = octopuses > 100 
    while (octopuses > 9).any():
        # Noting which octopus has flashed
        # Must happen before adding flashes
        has_flashed = np.logical_or(has_flashed, octopuses > 9)
        # Adding the flashes to the normal octopuses
        # This will increase some of the nullified octopuses
        # but they will not exceed 9 before being nullified again
        octopuses += convolve2d(octopuses > 9, B, "same")
        # Resetting the flashing octopuses
        octopuses[has_flashed] = 0

    # Adjust counters
    flashes += has_flashed.sum()
    step += 1

    if step == 100:
        print("Part 1:\t", flashes) 

print("Part 2:\t", step)
