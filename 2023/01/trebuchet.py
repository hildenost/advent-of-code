""" Advent of Code 2023. Day 1: Trebuchet?! """
import re

with open("input.txt") as f:
    calibrations = f.read()

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

pattern = f"(?=({'|'.join(digits)}))"

def add_digit(m):
    """In wordy number, insert the digit and the last letter of word"""
    return str(digits.index(m[1])) + m[1][-1]

def calibrate(calibrations, part=1):
    if part == 2:
        calibrations = re.sub(pattern, add_digit, calibrations)
    
    # Remove characters that are not a digit, keep newlines
    numbers = re.sub("[a-z]", "", calibrations)

    return sum(int(number[0] + number[-1]) for number in numbers.splitlines())

print("Part 1:\t", calibrate(calibrations))
print("Part 2:\t", calibrate(calibrations, part=2))
