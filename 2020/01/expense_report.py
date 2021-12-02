""" Advent of code 2020 Day 1: Report Repair """

import numpy as np


def sum_expenses(expenses, n=2, magic_number=2020):
    """ Find the `n` number of entries in a list of expenses that sum to `magic_number`.
    
    Numpy solution to exploit advanced indexing, sorting and searchsorted.

    Returns
    -------
    out : int
        The product of the `n` values that sum to `magic_number`

    """
    sorted_expenses = np.sort(expenses)

    # Creating the pivot indices, that is, the lowest values in the list
    # They will increase while searching for the complimentary value
    indices = np.arange(n - 1)

    # Running the loop as long as the rightmost marker is within list bounds
    while indices[-1] < len(sorted_expenses):
        # Computing the remainder
        remainder = magic_number - sorted_expenses[indices].sum()
        # And finding the index where the remainder would be placed
        k = np.searchsorted(sorted_expenses, remainder)

        # If that index k is 0
        if k == 0:
            indices = np.arange(indices[0] + 1, indices[0] + n)
            continue

        # If the remainder exists in the list, we have a winner!
        if remainder == sorted_expenses[k]:
            return sorted_expenses[[*indices, k]].prod()

        # Moving the rightmost marker one step up
        indices[-1] += 1

    print(f"Sorry, no {n} values in the list could sum up to {magic_number}")


test = np.array([1923, 1721, 979, 366, 299, 675, 1456])

with open("01\expenses.txt", "r") as f:
    report = np.sort(np.array([int(line) for line in f.readlines()]))

print(sum_expenses(np.sort(test)))
print(sum_expenses(np.sort(report)))

print(sum_expenses(np.sort(test), n=3))
print(sum_expenses(np.sort(report), n=3))
