""" Advent of Code 2016. Day 14: One-Time Pad """

from hashlib import md5
import re

SALT = "abc"

pattern = r"([a-f0-9])(\1)(\1)"


def pattern5(chars, key):
    return re.findall(f"({chars})(\\1)(\\1)(\\1)(\\1)", key)


def generate_key(stretch=1):
    hashes = {}
    i = 0
    N = 0
    while True:
        if i not in hashes:
            h = SALT + str(i)
            for __ in range(stretch):
                h = md5(h.encode()).hexdigest()
            hashes[i] = h

        m = re.findall(pattern, hashes[i])

        if m:
            for j in range(i + 1, i + 1000 + 1):
                if j not in hashes:
                    h = SALT + str(j)
                    for __ in range(stretch):
                        h = md5(h.encode()).hexdigest()
                    hashes[j] = h
                if pattern5(m[0][0], hashes[j]):
                    N += 1
                    break

        if N == 64:
            return i

        i += 1


print("Part 1:\t", generate_key())
print("Part 2:\t", generate_key(stretch=2017))
