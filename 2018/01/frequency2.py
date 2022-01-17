"""Advent of code 2018: 2/2 on 1 Dec

Finding and printing first repeated frequency.

"""
import sys


def find_duplicate_frequency():
    """Function reads from standard input and returns
    the first duplicate frequency.

    Optimized version: The first repeated value must be one of the
    cumulated sums during the first run. The cumulated sum is therefore
    only found once.
    """
    lines = [int(line) for line in sys.stdin.readlines()]

    frequency = 0
    possible_frequencies = [frequency]
    is_initial_run = True

    while True:
        for line in lines:
            frequency += line

            if frequency in possible_frequencies:
                return frequency

            if is_initial_run:
                possible_frequencies.append(frequency)
        is_initial_run = False


print(find_duplicate_frequency())
