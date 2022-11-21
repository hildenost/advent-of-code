""" Advent of Code 2019 Day 16: Flawed Frequency Transmission """

import numpy as np

signal = np.arange(1, 9)

msg = "secret"
signal = np.array([int(n) for n in msg])

def to_string(array):
    return "".join(str(a) for a in array)

def fft(signal, repeats=1):
    signal = np.tile(signal, repeats)
    idx = 0 if repeats == 1 else int(to_string(signal[:7]))

    # For part 2, only the part of signal starting from
    # the special index is needed
    signal = signal[idx:]

    for __ in range(100):
        cumsums = signal[::-1].cumsum()[::-1]
        temp = cumsums.copy()

        # Part 2
        # Since the starting index we're looking for is in the second half
        # of the signal, this problem simplifies to only the cumulative sum
        # of the signal, starting from behind.
        if repeats == 1:
            for i in range(1, len(signal)):
                selected = cumsums[i::i+1]
                sgn = (-1)**((i+1)*i//2)
                temp[:len(selected)] += sgn * selected

        signal = abs(temp) % 10
    return to_string(signal[:8])

print("Part 1:\t", fft(signal)) 
print("Part 2:\t", fft(signal, repeats=10000)) 

