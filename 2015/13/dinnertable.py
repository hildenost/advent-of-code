""" Advent of Code 2015. Day 13: Knights of the Dinner Table """
import re
import numpy as np
from collections import defaultdict


test = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.""".splitlines()

with open("13/input.txt") as f:
    test = f.read().splitlines()

from itertools import combinations


def convert_input_to_dist(guestlist, add_me=False):
    size = int(np.ceil(np.sqrt(len(guestlist))))

    units = [
        int(x) if gain == "gain" else -int(x)
        for gain, x in re.findall(r"(gain|lose) (\d+)", "\n".join(test))
    ]

    dist = np.zeros((size, size), dtype=int)
    for row in range(size):
        idc = [x for x in range(size) if x != row]
        dist[row, idc] = units[row * (size - 1) : (row + 1) * (size - 1)]

    # Adding the transposed distance matrix to get the total sum
    # of the happiness weight between two guests
    dist += dist.T

    if add_me:
        # Increase dist matrix with extra rows and columns of 0s
        # Must be at the start of the dist matrix, or else it doesn't
        # change the end result
        size += 1
        me_dist = np.zeros((size, size), dtype=int)
        me_dist[1:, 1:] = dist
        return me_dist

    return dist


def tsp(dist):
    """ Traveling salesman """
    size = dist.shape[0]

    cost = {(frozenset({0}), 0): 0}
    for s in range(2, size + 1):
        for subset in combinations(range(1, size), s - 1):
            subset = frozenset([0, *subset])
            cost[subset, 0] = 0
            for i in subset:
                if i == 0:
                    continue
                cost[subset - {i}, 0] = 0
                cost[subset, i] = max(
                    cost[subset - {i}, j] + dist[i, j] for j in subset if i != j
                )
    return max(
        cost[frozenset(range(size)), j] + dist[0, j] for j in range(size) if j != 0
    )


print("Part 1: ", tsp(convert_input_to_dist(test)))
print("Part 2: ", tsp(convert_input_to_dist(test, add_me=True)))

