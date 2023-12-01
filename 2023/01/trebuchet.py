""" Advent of Code 2023. Day 1: Trebuchet?! """
import re

with open("input.txt") as f:
    calibration = f.read().splitlines()

DIGITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

reverse = [d[::-1] for d in DIGITS]

pattern = r"\d|" + "|".join(DIGITS)
revpattern = r"\d|" + "|".join(reverse)

answer = 0
for line in calibration:
    pattern = r"\d|" + "|".join(DIGITS)
    digits = re.findall(pattern, line)
    first = digits[0]
    last = re.findall(revpattern, line[::-1])[0]

    if first in DIGITS:
        first = str(DIGITS.index(first))
    if last in reverse:
        last = str(reverse.index(last))

    answer += int(str(first) + str(last))

print(answer)
