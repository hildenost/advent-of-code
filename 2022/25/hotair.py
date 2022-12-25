""" Advent of Code 2022. Day 25: Full of Hot Air """


with open("input.txt") as f:
    fuel = f.read().splitlines()

snafus = {
 "2": 2,
 "1": 1,
 "0": 0,
 "-": -1,
 "=": -2
}
deces = {
 2: "2",
 1: "1",
 0: "0",
 3: "=",
 4: "-",
}

def snafu2dec(snafu):
    return sum(snafus[digit] * 5**i for i, digit in enumerate(snafu[::-1]))

def dec2snafu(dec):
    ufans = ""
    i = 0
    while dec != snafu2dec(ufans[::-1]):
        ufans += deces[round(dec/5**i) % 5]
        i += 1
    return ufans[::-1]

total = sum(snafu2dec(line) for line in fuel)

print("Part 1:\t", dec2snafu(total))
