""" Advent of Code 2023. Day 4: Scratchcards """
from collections import defaultdict

with open("input.txt") as f:
    cards = f.readlines()

instances = defaultdict(lambda: 1)

points = 0
for i, card in enumerate(cards, 1):
    numbers = card.split()
    winning = {int(j) for j in numbers[2:12]}
    yours = {int(j) for j in numbers[13:]}

    n = len(winning & yours)

    points += 2 ** (n - 1) if n > 0 else 0

    p = instances[i]
    for j in range(i + 1, i + 1 + n):
        instances[j] += p * 1
print("Part 1:\t", points)
print("Part 2:\t", sum(instances.values()))
