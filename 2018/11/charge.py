""" Advent of Code 2018. Day 11: Chronal Charge """
import numpy as np
from scipy.signal import convolve

SERIAL_NO = 5153

def power_level(x, y):
    rack_id = x + 10
    power = rack_id * y + SERIAL_NO
    power *= rack_id
    # Get the hundreds digit
    power = (power // 100) % 10
    return power - 5

x = np.arange(300)
y = np.arange(300)

power = power_level(*np.ix_(x, y))

B = np.ones((3, 3), dtype=int)

# This matrix will have size - 2 compared to the power
# matrix.
# What was (1, 1) in power, is (0, 0) here
fuel = convolve(power, B, mode="valid")

# Therefore, the indices here are automatically adjusted
# for the otherwise off-by-one-error
x, y = np.unravel_index(fuel.argmax(), fuel.shape)

print("Part 1:\t", f"{x},{y}")

# Testing out various sizes
max_power = 0
xmax, ymax = (0, 0)
for size in range(1, 301):
    B = np.ones((size, size), dtype=int)
    fuel = convolve(power, B, mode="valid")
    if fuel.max() > max_power:
        xmax, ymax = np.unravel_index(fuel.argmax(), fuel.shape)
        max_power = fuel.max()
        s = size
print("Part 2:\t", f"{xmax},{ymax},{s}")

