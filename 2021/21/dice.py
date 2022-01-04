""" Advent of Code 2021. Day 21: Dirac Dice """

from itertools import product
from collections import Counter


player1 = (8, 0)
player2 = (7, 0)


def dice():
    i = 1
    while True:
        yield 3 * (i + 1)
        i += 3


def walk(player, steps):
    res = (player + steps) % 10
    return 10 if res == 0 else res


player1 = (8, 0)
player2 = (7, 0)


def play_deterministic(player1, player2):
    d = dice()
    for i, throw in enumerate(d):
        if i % 2:
            move = walk(player2[0], throw)
            player2 = (move, player2[1] + move)
            if player2[1] >= 1000:
                return 3 * (i + 1) * player1[1]
        else:
            move = walk(player1[0], throw)
            player1 = (move, player1[1] + move)
            if player1[1] >= 1000:
                return 3 * (i + 1) * player2[1]


print("Part 1:\t", play_deterministic(player1, player2))

dirac = Counter([sum(x) for x in product((1, 2, 3), repeat=3)])

wins = [0, 0]


def play(player1, player2, counts=1, turn=0):
    global wins

    if player1[1] >= 20 and turn % 2 == 0:
        # Gonna win regardless
        wins[0] += counts * sum(dirac.values())
        return

    if player2[1] >= 20 and turn % 2:
        # Gonna win regardless
        wins[1] += counts * sum(dirac.values())
        return

    for steps, freq in dirac.items():

        if turn % 2:
            move = walk(player2[0], steps)
            p1 = player1
            p2 = (move, player2[1] + move)
            if p2[1] >= 21:
                wins[1] += freq * counts
                continue
        else:
            move = walk(player1[0], steps)
            p1 = (move, player1[1] + move)
            p2 = player2

            if p1[1] >= 21:
                wins[0] += freq * counts
                continue
        play(p1, p2, counts * freq, turn + 1)


play(player1, player2)
print("Part 2:\t", max(wins))
