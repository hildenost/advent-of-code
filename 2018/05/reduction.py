""" Advent of Code 2018. Day 5: Alchemical Reduction """

with open("input.txt") as f:
    polymer = f.read().strip()

def is_equal_and_opposite(a, b):
    """ If difference in Ascii value is
    32, then a and b are the same letter in opposite cases.

    """
    return abs(ord(a)-ord(b)) == 32

def react(polymer, ignore=""):
    stack = [polymer[0]]
    for p in polymer[1:]:
        if p.lower() == ignore:
            continue
        elif is_equal_and_opposite(p, stack[-1]):
            stack.pop()
        else:
            stack.append(p)
    return len(stack)

print("Part 1:\t", react(polymer))

print("Part 2:\t", min(react(polymer, ignore=letter) for letter in "abcdefghijklmnopqrstuvwxyz"))
