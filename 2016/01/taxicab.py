""" Advent of Code 2016. Day 1: No Time for a Taxicab """
import numpy as np

with open("input.txt") as f:
  dirs = [d.strip() for d in f.read().split(",")]

# North and East are positive
# face are: north = 0, east = 1, south = 2, west = 3
turn = {
  "L": lambda x: (x-1) % 4,
  "R": lambda x: (x+1) % 4
}

def move(dirs, part=1):
  face = 0 # north
  pos = [0, 0]
  seen = {tuple(pos)}

  for t, *blocks in dirs:
    face = turn[t](face)

    idx = face % 2

    sign = (idx + 1 - face)
    to_go = int("".join(blocks))

    final = pos[idx] + sign * to_go

    if part == 1:
      pos[idx] = final 

    while pos[idx] != final:
      pos[idx] += sign

      if tuple(pos) in seen:
        return sum(np.abs(pos))

      seen.add(tuple(pos))
  return sum(np.abs(pos))

print("Part 1:\t", move(dirs)) 
print("Part 2:\t", move(dirs, part=2)) 
