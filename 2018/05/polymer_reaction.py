""" Day 5: Alchemical Reaction.

"""
import sys

def is_equal_and_opposite(a, b):
    """ If difference in Ascii value is
    32, then a and b are the same letter in opposite cases.

    """
    return abs(ord(a)-ord(b)) == 32

def polymer_reaction(polymer):
    """ Removing equal, but opposite components of a polymer. """
    i = 0
    while i < len(polymer)-1:
        if is_equal_and_opposite(polymer[i], polymer[i+1]):
            polymer = polymer[:i] + polymer[i+2:]
            i -= 1
        else:
            i += 1
    return len(polymer)

def length_improved(letter, polymer):
    """ Returns the length of improved polymer. """
    polymer = polymer.replace(letter, "")
    polymer = polymer.replace(letter.upper(), "")
    return polymer_reaction(polymer)

def improved_reaction(polymer):
    """ Finds the minimum length polymer after removing one type. """
    return min((length_improved(letter, polymer)
                for letter in "abcdefghijklmnopqrstuvwxyz"))

INPUT = sys.stdin.read().strip()
print(polymer_reaction(INPUT))
print(improved_reaction(INPUT))
