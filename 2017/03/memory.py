""" Advent of Code 2017. Day 3: Spiral Memory """
import math

# Each layer of square has side lengths equal to the odd numbers
# 1, 3, 5, ...
# To find out which square a number belongs to, take the square
# and round the result upwards to the next odd number

puzzle_input = 347991

def get_n(number):
    temp = math.ceil(math.sqrt(number))
    return temp + (1 - temp % 2)

square = get_n(puzzle_input) 
last_number = (square - 2)**2
quadrant_size = square - 1 
remainder = puzzle_input - last_number
quadrant = math.ceil(remainder / quadrant_size)
distance = (1 - quadrant) * quadrant_size + remainder

print("Part 1:\t", distance)

neighbours = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]
# Turns
# 0, 0, 1, 1, 2, 2, 3, 3, 4, 4
def get_sum(x, y):
    return sum(
        grid.get((x+ddx, y+ddy), 0)
        for ddx, ddy in neighbours)

def spiral(limit):
    n = 0
    x, y = 0, 0
    grid = {(x, y): 1}

    def get_sum(x, y):
        return sum(
            grid.get((x+ddx, y+ddy), 0)
            for ddx, ddy in neighbours)

    while True:
        n += 1

        sign = (-1)**(n-1)
        for dx in range(1, n+1):
            value = get_sum(x+sign*dx, y)
            if value > limit:
                return value
            grid[(x+sign*dx, y)] = value

        x += sign*n

        for dy in range(1, n+1):
            value = get_sum(x, y+sign*dy)
            if value > limit:
                return value

            grid[(x, y+sign*dy)] = value

        y += sign*n

print("Part 2:\t", spiral(puzzle_input))
