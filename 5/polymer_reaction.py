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
    return polymer

print(len(polymer_reaction(sys.stdin.read().strip())))
