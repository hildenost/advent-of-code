"""Part 2 of Day 2: Inventory Management System."""
import sys
from itertools import combinations

def find_prototype_fabric_boxes():
    """ Brute force solution.

    Creating all possiblie combinations of words, then
    comparing the letters.

    """

    lines = [line.rstrip("\n") for line in sys.stdin.readlines()]
    word_length = len(lines[0])
    pairs = combinations(lines, 2)
    for pair in pairs:
        common_letters = letter_diff(*pair)
        if len(common_letters) == word_length - 1:
            return "".join(common_letters)

def letter_diff(first, second):
    """ Return a list of common letters at same spot in two words. """
    return [first_letter
            for first_letter, second_letter in zip(first, second)
            if first_letter == second_letter]

print(find_prototype_fabric_boxes())
