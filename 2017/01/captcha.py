""" Advent of Code 2017. Day 1: Inverse Captcha """

def captcha(sequence, steps=1):
    return sum(
        int(a) for a, b in zip(sequence, sequence[steps:] + sequence[:steps])
        if a == b
    )

with open("input.txt") as f:
    sequence = f.read().strip()

print("Part 1:\t", captcha(sequence))
print("Part 2:\t", captcha(sequence, steps=len(sequence)//2))
