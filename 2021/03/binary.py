""" Advent of Code 2021. Day 3: Binary Diagnostic """

import numpy as np

with open("input.txt") as f:
  diagnostic = np.array(
    [
    [int(l) for l in line]
    for line in f.read().splitlines()
    ]
  )

print(diagnostic)

gamma_mask = diagnostic.sum(axis=0) > diagnostic.shape[0] / 2

gamma = int("".join(str(int(m)) for m in gamma_mask), 2)
epsilon = int("".join(str(int(m)) for m in ~gamma_mask), 2)

print(gamma * epsilon)

#part 2
gamma_mask = diagnostic.sum(axis=0) >= diagnostic.shape[0] / 2

oxygen = diagnostic

i = 0
while len(oxygen) > 1:
  oxygen = oxygen[oxygen[:, i] == gamma_mask[i]] 
  i += 1
oxygen_rating = int("".join(str(o) for o in oxygen[0]), 2)

co2 = diagnostic
i = 0
while len(co2) > 1:
  co2 = co2[co2[:, i] == ~gamma_mask[i]] 
  print(co2, ~gamma_mask)
  i += 1
print(co2)
co2_rating = int("".join(str(o) for o in co2[0]), 2)
print(co2_rating * oxygen_rating)


  
