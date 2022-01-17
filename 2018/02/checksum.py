import sys
from collections import defaultdict


def checksum():
    twos = 0
    threes = 0

    for line in sys.stdin.readlines():
        letter_counts = defaultdict(int)

        for letter in line:
            letter_counts[letter] += 1

        if 2 in letter_counts.values():
            twos += 1
        if 3 in letter_counts.values():
            threes += 1

    return twos * threes

print(checksum())
