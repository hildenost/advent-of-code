""" Advent of Code 2020 Day 3: Toboggan Trajectory """
import numpy as np

test_map = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

with open("03/map.txt") as f:
    tree_map = f.read().splitlines()

height = len(tree_map)

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def count_trees(the_map, slopes):
    def convert(x):
        return x % len(tree_map[0])

    return np.array(
        [
            sum(
                tree_map[y][convert(right * y // down)] == "#"
                for y in range(0, height, down)
            )
            for right, down in slopes
        ]
    )


print(count_trees(tree_map, SLOPES).prod())

