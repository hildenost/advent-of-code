""" Advent of Code 2023. Day 7: Camel Cards """


def is_five(hand):
    cards = set(list(hand))

    if len(cards) == 2 and "J" in hand:
        # We can transform all jokers to the other value
        # To get 5 of a kind
        return True

    return len(cards) == 1


def is_four(hand):
    cards = set(list(hand))
    counts = [hand.count(c) for c in cards]

    if "J" in hand and len(cards) == 3:
        # We can only get 4 of a kind with jokers if there is
        # 3 different cards where one is the jokers
        # The amount of jokers plus the maximum of the other cards
        # should be 4
        jokers = hand.count("J")
        return any(jokers + c == 4 for c in counts)

    # If there is a joker, either 1 or 4, it will already have
    # been used to make 5 of a kind
    return 4 in counts


def is_house(hand):
    cards = set(list(hand))
    counts = [hand.count(c) for c in cards]

    if "J" in hand and len(cards) == 3 and 2 in counts:
        return True

    return len(cards) == 2 and 2 in counts


def is_three(hand):
    cards = set(list(hand))
    counts = [hand.count(c) for c in cards]

    if "J" in hand and len(cards) == 4:
        return True

    return len(cards) == 3 and 3 in counts


def is_two_pair(hand):
    cards = set(list(hand))
    # Det var det, hvis joker her, så er den brukt opp på tre like
    return len(cards) == 3


def is_one_pair(hand):
    cards = set(list(hand))
    if "J" in hand and len(cards) == 5:
        return True

    return len(cards) == 4


hands = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".splitlines()

with open("input.txt") as f:
    hands = f.readlines()

from collections import defaultdict

types = defaultdict(list)
for line in hands:
    hand, bid = line.split()

    if is_five(hand):
        types["five"].append((hand, bid))
    elif is_four(hand):
        types["four"].append((hand, bid))
    elif is_house(hand):
        types["house"].append((hand, bid))
    elif is_three(hand):
        types["three"].append((hand, bid))
    elif is_two_pair(hand):
        types["twopair"].append((hand, bid))
    elif is_one_pair(hand):
        types["pair"].append((hand, bid))
    else:
        types["high"].append((hand, bid))


def transform(hand, jvalue=11):
    hand = tuple(hand)
    conv = {"A": 14, "K": 13, "Q": 12, "J": jvalue, "T": 10}
    hand = tuple(int(c) if c.isdigit() else conv[c] for c in hand)
    return hand


winnings = 0
rank = 1
for k in ["high", "pair", "twopair", "three", "house", "four", "five"]:
    hands = sorted([(transform(hand, jvalue=0), bid) for hand, bid in types[k]])

    for hand, bid in hands:
        winnings += rank * int(bid)
        rank += 1


print(winnings)
