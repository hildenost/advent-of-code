""" Advent of Code 2022. Day 3: Rucksack Reorganization """

with open("input.txt") as f:
    rucksacks = f.read().splitlines()

items = ""
for rucksack in rucksacks:
    r = len(rucksack) // 2
    items += set(rucksack[r:]).intersection(set(rucksack[:r])).pop()

priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Part 1:\t", sum(priorities.find(l) for l in items))

badges = [] 
for i in range(0, len(rucksacks), 3):
    first, *rest = [set(s) for s in rucksacks[i:i+3]]
    badges.append(first.intersection(*rest).pop())

print("Part 2:\t", sum(priorities.find(l) for l in badges))
