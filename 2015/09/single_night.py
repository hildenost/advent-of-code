""" Advent of Code 2015 Day 9: All in a Single Night """

example = """\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".splitlines()

with open("input.txt") as f:
    example = f.read().splitlines()

distances = {}
cities = set()

# Parsing input
for line in example:
    A, __, B, __, distance = line.split()
    cities.update({A, B})

    # Storing the distance between the two cities
    # in the distance dict, using a frozenset as key
    distances[frozenset((A, B))] = int(distance)

from itertools import permutations

# Initializing the end points
shortest = sum(list(distances.values()))
longest = 0

# Iterating over all permutations of the city visiting order
for X in permutations(cities, len(cities)):
  # Storing the resulting distance of that particular route 
  dist = sum(distances[frozenset({X[i], X[i+1]})] for i in range(len(cities)-1))

  shortest = min(shortest, dist) 
  longest = max(longest, dist)

print("Part 1: ", shortest)
print("Part 2: ", longest)
  


