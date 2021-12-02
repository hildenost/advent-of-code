""" Advent of Code 2015. Day 16: Aunt Sue """

recent_sue = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1
}

import re

with open("input.txt") as f:
  raw_sues = f.read().splitlines()

original_sues = [
  {k: int(v) for k,v in re.findall(r"([a-z]+?): (\d+)", sue)}
  for sue in raw_sues
]

def is_valid_part1(thing, sue, recent_sue):
  return sue[thing] == recent_sue[thing]

def is_valid_part2(thing, sue, recent_sue):
  if thing in ["cats", "trees"]:
    return sue[thing] > recent_sue[thing]
  elif thing in ["pomeranians", "goldfish"]:
    return sue[thing] < recent_sue[thing]
  return sue[thing] == recent_sue[thing]

def find_sue(recent_sue, sues, part=1):
  valid = is_valid_part1 if part == 1 else is_valid_part2
  # filtering
  for thing in recent_sue:
    sues = [
      sue for sue in sues
      if thing not in sue
      or valid(thing, sue, recent_sue) 
      ]
  return sues[0] 

def get_sue_number(sues, sue):
  return sues.index(sue) + 1

print("Part 1: ", get_sue_number(original_sues, find_sue(recent_sue, original_sues)))
print("Part 2: ", get_sue_number(original_sues, find_sue(recent_sue, original_sues, part=2)))
