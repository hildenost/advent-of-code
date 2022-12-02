""" Advent of Code 2022. Day 2: Rock Paper Scissors """

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 1
DRAW = 2
WIN = 3

with open("input.txt") as f:
    rounds = [
        [ROCK if l in "AX" else PAPER if l in "BY" else SCISSORS for l in line.split()]
        for line in f.readlines()
    ]


def is_win_for_me(opp, me):
    return (opp, me) in [(SCISSORS, ROCK), (PAPER, SCISSORS), (ROCK, PAPER)]


def score(opp, me):
    return me + 6 * is_win_for_me(opp, me) + 3 * (me == opp)


print("Part 1:\t", sum(score(*r) for r in rounds))

shape = {LOSE: lambda x: 1 + (x - 2) % 3, DRAW: lambda x: x, WIN: lambda x: 1 + x % 3}

print("Part 2:\t", sum([score(opp, shape[strategy](opp)) for opp, strategy in rounds]))
