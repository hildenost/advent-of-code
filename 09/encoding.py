""" Advent of Code 2020 Day 9: Encoding Error """
import numpy as np

number_list = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]

len_preamble = 5

with open("09/input.txt") as f:
    number_list = [int(n) for n in f.read().splitlines()]
len_preamble = 25


def check_valid(number, preamble):
    sorted_preamble = np.sort(preamble)
    i = 0
    while i < len(preamble):
        remainder = number - sorted_preamble[i]
        k = np.searchsorted(sorted_preamble, remainder)

        if k < len(preamble) and remainder == sorted_preamble[k]:
            return True
        i += 1
    return False


def find_invalid(numbers, len_preamble):
    pos = len_preamble
    while check_valid(numbers[pos], numbers[pos - len_preamble : pos]):
        pos += 1
    return pos


### PART 1
invalid_idx = find_invalid(number_list, len_preamble)
invalid_number = number_list[invalid_idx]
print(invalid_number)

### PART 2
for num_numbers in range(2, len(number_list[:invalid_idx])):
    sums = np.convolve(
        number_list[:invalid_idx], np.ones(num_numbers, dtype=int), "valid"
    )
    k = np.searchsorted(sums, invalid_number)
    if sums[k] == invalid_number:
        numbers = number_list[k : k + num_numbers]
        print(max(numbers) + min(numbers))
        break

