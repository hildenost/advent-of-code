""" Advent of Code 2015. Day 19: Medicine for Rudolph """
import re

RULES = [
  ("H", "HO"),
  ("H", "OH"),
  ("O", "HH"),
  ]

medicine = "HOH"

with open("input.txt") as f:
  lines = f.read().splitlines()

RULES = [line.split()[::2] for line in lines[:-2]]
medicine = lines[-1]


molecules = {
  medicine[:m.start()] + repl + medicine[m.end():]
  for l, repl in RULES
  for m in re.finditer(l, medicine)
} 

print("PART 1:\t", len(molecules))

### PART 2
# Always starting with e
# Observations:
# Some rules are on the form of XxRn(...)Ar
# In other words, I should treat them as:
# Rn -> (
# Ar -> )

# First, inverting the rulebook
rules = {b: a for a, b in RULES}


# Keeps track of the indices of the opening bracket "Rn"
rns = []

# This should hold the final answer
counter = 0

# The pointer
i = 0

while medicine != "e":
  if i >= len(medicine):
    for key in rules:
      (medicine, n) = re.subn(key, rules[key], medicine)
      counter += n

  if medicine[i:i+2] == "Ar":
    rn = rns.pop()

    sub_m = medicine[rn:i+2]
    if sub_m.startswith("Ca"):
      # Correcting for one edge case
      rn -= 2
      sub_m = medicine[rn:i+2]

    while sub_m not in rules.values():
      for key in rules:
        (sub_m, n) = re.subn(key, rules[key], sub_m)
        counter += n
        
    medicine = medicine[:rn] + sub_m + medicine[i+2:]
    i = rn
  #elif m is not None:
  elif (m := re.match(r"^[A-Z][a-z]?Rn", medicine[i:])) is not None:
    # Adding Rn to stack
    rns.append(i + m.start())
    i += m.end()
  else:
    i += 1

print("PART 2:\t", counter)
