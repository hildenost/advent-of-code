""" Advent of Code 2023. Day 2: Cube Conundrum """
import re

limits = dict(red=12, green=13, blue=14)

with open("input.txt") as f:
    games = f.read().splitlines()

possible = sum(i + 1 for i in range(len(games)))
for game in games:
    n, cubes = game.split(":")
    n = int(re.findall(r"\d+", n)[0])
    for subset in cubes.split(";"):
        cubes = re.findall(r"(\d+) (blue|red|green)", subset)
        check = [int(i) > limits[color] for i, color in cubes]
        if any(check):
            possible -= n
print("Part 1:\t", possible)


power = 0
for game in games:
    n, cubes = game.split(":")
    n = int(re.findall(r"\d+", n)[0])
    cubes = re.findall(r"(\d+) (blue|red|green)", cubes)
    blue = max(int(i) for i, col in cubes if col == "blue")
    green = max(int(i) for i, col in cubes if col == "green")
    red = max(int(i) for i, col in cubes if col == "red")
    power += blue * green * red
print("Part 2:\t", power)
