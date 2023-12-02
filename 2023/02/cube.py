""" Advent of Code 2023. Day 2: Cube Conundrum """
import re


with open("input.txt") as f:
    games = f.read().splitlines()


def get_max(cubes, color):
    return max(int(i) for i, col in cubes if col == color)


limits = dict(red=12, green=13, blue=14)
possible = 0
power = 0
for n, game in enumerate(games, 1):
    cubes = re.findall(r"(\d+) (blue|red|green)", game)

    blue = get_max(cubes, "blue")
    green = get_max(cubes, "green")
    red = get_max(cubes, "red")

    if blue <= limits["blue"] and green <= limits["green"] and red <= limits["red"]:
        possible += n

    power += blue * green * red

print("Part 1:\t", possible)
print("Part 2:\t", power)
