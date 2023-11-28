""" Advent of Code 2019. Day 22: Slam Shuffle """


def deal(deck):
    return deck[::-1]

def cut(deck, N): 
    return deck[N:] + deck[:N]

def dealN(deck, N):
    new_deck = [None for __ in deck]
    for i, card in enumerate(deck):
        new_deck[(i * N) % len(deck)] = card

    return new_deck

sample = """\
deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
""".splitlines()


def shuffle(process, cards=10007):
    deck = [n for n in range(cards)]
    print(deck)
    for line in process:
        first, *__, last = line.split()

        if last == "stack":
            deck = deal(deck)
        elif first == "deal":
            deck = dealN(deck, int(last))
        else:
            deck = cut(deck, int(last))
        print(deck)

    return deck

with open("input.txt") as f:
    instructions = f.read().splitlines()
#print("Part 1:\t", shuffle(instructions).index(2019))

# Find new position based on action
def new_deal(pos, size_deck):
    return size_deck - pos - 1

def new_cut(pos, size_deck, N):
    return (pos - N) % size_deck

def new_dealN(pos, size_deck, N):
    return (N*pos) % size_deck

# Find prev position based on action
def prev_deal(new_pos, size_deck):
    return size_deck - new_pos - 1

def prev_cut(new_pos, size_deck, N):
    return (new_pos + N) % size_deck

def prev_dealN(new_pos, size_deck, N):
    """
    Modular magic ahead

    The new position is computed by:
    (1)     new_pos = (prev_pos * N) % size_deck
    Since new_pos < size_deck, new_pos = new_pos % size_deck

    Therefore, the difference
    (2)     new_pos - prev_pos * N = k * size_deck
    where k is an integer.

    Let's solve for prev_pos:
    (3)     prev_pos = (new_pos - k * size_deck) / N

    To make sure that we have our true prev_pos, we take the modulus of (3),
    so that the full equation to find the prev_pos is:
    (4)     prev_pos = ((new_pos - k * size_deck) / N) % size_deck
    """
    for k in range(size_deck):
        pos = (new_pos - k * size_deck) / N
        if pos.is_integer():
            return int(pos) % size_deck

    
deck = [n for n in range(10)]
print(deck)
print(dealN(deck, 7))
print(prev_dealN(4, 10, 7))

# Idea:
# Go backwards through the process

# Find the position of the card that ends up in 2020
# Find the position that card had the step before
# Find the position that card had the step before
# Find the position that card had the step before
# etc
# Find the starting position of that card


def unshuffle(process, pos=2020, cards=119315717514047):
    for line in process[::-1]:
        first, *__, last = line.split()
        if last == "stack":
            pos = prev_deal(pos, cards)
        elif first == "deal":
            pos = prev_dealN(pos, cards, int(last))
        else:
            pos = prev_cut(pos, cards, int(last))
    return pos

cards=119315717514047
pos = 2020
deltas = set()
for __ in range(1000000):
    new_pos = unshuffle(instructions, pos=pos)
    print((new_pos-pos) % cards)
    if (new_pos-pos) % cards in deltas:
        print("SAME DIFF!!!!")
        input()
    deltas.add((new_pos-pos) % cards)
    pos = new_pos
# 119315717514047 cards
# 101741582076661 times

# 95156681699816 too high
# 95156681699771 too high
# 55836183599565 too low


