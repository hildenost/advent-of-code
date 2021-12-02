""" Advent of Code 2016. Day 2: Bathroom Security """


instructions = """ULL
RRDDD
LURDL
UUUUD
""".splitlines()

with open("input.txt") as f:
  instructions = f.read().splitlines()

keypad = {
#key: [u, d, l, r]
  1: [1, 4, 1, 2],
  2: [2, 5, 1, 3],
  3: [3, 6, 2, 3],
  4: [1, 7, 4, 5],
  5: [2, 8, 4, 6],
  6: [3, 9, 5, 6],
  7: [4, 7, 7, 8],
  8: [5, 8, 7, 9],
  9: [6, 9, 8, 9]
}

keypad2 = {
#key: [u, d, l, r]
  1: [1, 3, 1, 1],
  2: [2, 6, 2, 3],
  3: [1, 7, 2, 4],
  4: [4, 8, 3, 4],
  5: [5, 5, 5, 6],
  6: [2, "A", 5, 7],
  7: [3, "B", 6, 8],
  8: [4, "C", 7, 9],
  9: [9, 9, 8, 9],
  "A": [6, "A", "A", "B"],
  "B": [7, "D", "A", "C"],
  "C": [8, "C", "B", "C"],
  "D": ["B", "D", "D", "D"]
}
moves = {
    "U": 0, 
    "D": 1, 
    "L": 2,  
    "R": 3 
}

def find_code(instructions, keypad):
  code = []
  key = 5
  for instruction in instructions:
    for i in instruction:
      key = keypad[key][moves[i]]
    code.append(str(key))
  return "".join(code)
print("Part 1:\t", find_code(instructions, keypad))
print("Part 2:\t", find_code(instructions, keypad2))
