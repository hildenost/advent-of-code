""" Advent of Code 2015. Day 18: Like a GIF For Your Yard """

import re

with open("input.txt") as f:
    lines = f.read().splitlines()


grid = [list(row) for row in lines]


#grid = [
#  list("##.#.#"),
#  list("...##."),
#  list("#....#"),
#  list("..#..."),
#  list("#.#..#"),
#  list("####.#"),
#]
STEPS = 100


# ON (#) stays ON when 2 OR 3 neighbours ON, otherwise OFF
# OFF (.) turns ON when 3 neighbours ONE, otherwise OFF


DIRS = [
  (-1, -1),
  (-1, 0),
  (-1, 1),
  (0, -1),
  (0, 1),
  (1, -1),
  (1, 0),
  (1, 1)
]

def count_neighbours(i, j, grid):
  return sum(
    grid[i+dx][j+dy] == "#"
    for dx, dy in DIRS
    if 0 <= i + dx < len(grid)
    and 0 <= j + dy < len(grid)
  )

STUCK_LIGHTS = {(0,0), (0, len(grid)-1), (len(grid)-1, len(grid)-1), (len(grid)-1, 0)}

def step(grid, part2=False):
  new_grid = [list("."*len(grid)) for __ in range(len(grid))]

  for i, row in enumerate(grid):
    for j, col in enumerate(row):
      if part2 and (i, j) in STUCK_LIGHTS:
        new_grid[i][j] = "#"
        continue
      n = count_neighbours(i, j, grid)
      if (col == "#" and n in [2, 3]) or (col == "." and n == 3):
        new_grid[i][j] = "#"
  return new_grid

def count_lights(grid):
  return sum(light == "#" for row in grid for light in row)


      
def game_of_life(grid, steps, part2=False):
  if part2:
    for x, y in STUCK_LIGHTS:
      grid[x][y] = "#"

  for __ in range(steps):
    grid = step(grid, part2)

  return grid

print("PART 1: \t", count_lights(game_of_life(grid, STEPS)))
print("PART 2: \t", count_lights(game_of_life(grid, STEPS, part2=True)))


