""" Advent of Code 2017. Day 4: High-Entropy Passphrases """

import re
from collections import Counter

def is_valid(phrase):
    words = phrase.split()
    return len(words) == len(set(words))

def is_this_valid(phrase):
    words = set(tuple(sorted(list(ws))) for ws in phrase.split())
    return len(words) == len(phrase.split())

with open("input.txt") as f:
    passwords = f.read().splitlines()


print("Part 1:\t", sum(is_valid(password) for password in passwords))
print("Part 2:\t", sum(is_this_valid(password) for password in passwords))

