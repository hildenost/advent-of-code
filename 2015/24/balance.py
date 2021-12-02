""" Advent of Code 2015. Day 24: It Hangs in the Balance """

packages = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61,
      67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

from itertools import combinations
import math

def find_minimum_qe(k):
  capacity = sum(packages) / k

  for i in range(len(packages)):
    valid = list(c for c in combinations(packages, i+1) if sum(c) == capacity)
    if valid:
       return min(math.prod(v) for v in valid)

print("Part 1:\t", find_minimum_qe(k=3))
print("Part 2:\t", find_minimum_qe(k=4))
