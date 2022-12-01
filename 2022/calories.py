""" Advent of Code 2022. Day 1: Calorie Counting """

with open("input.txt") as f:
    calories = [sum(int(b) for b in a.split()) for a in f.read().split("\n\n")]

print(f"Part 1:\t{max(calories)}")

print(f"Part 2:\t{sum(sorted(calories, reverse=True)[:3])}")
