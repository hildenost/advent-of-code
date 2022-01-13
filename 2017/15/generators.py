""" Advent of Code 2017. Day 15: Dueling Generators """

# The divisor = 2147483647 = 2 ** 31 - 1
# This could mean something, but I didn't take advantage of it
divisor = 2147483647 

def generator(value, factor, multiple=1):
    while True:
        value = (value * factor) % divisor
        if value % multiple == 0:
            # Taking just the 16 first bits
            # equals a modulo 2**16 operation
            yield value % 2**16

from itertools import takewhile
def compare(As, Bs, STOP=10000):
    counter = 0
    for i, (a, b) in enumerate(zip(As, Bs)):
        if i > STOP:
            break

        counter += a == b
    return counter

As = generator(722, 16807)
Bs = generator(354, 48271)
import time
tic = time.perf_counter()
print("Part 1:\t", compare(As, Bs, 40_000_000))
toc = time.perf_counter()
print(f"{(toc-tic) / 60:6.2f} min")

As = generator(722, 16807, multiple=4)
Bs = generator(354, 48271, multiple=8)
tic = time.perf_counter()
print("Part 2:\t", compare(As, Bs, 5_000_000))
toc = time.perf_counter()
print(f"{(toc-tic) / 60:6.2f} min")
