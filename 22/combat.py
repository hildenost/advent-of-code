from collections import deque

test = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

with open("22/input.txt") as f:
    test = f.read()


def parse_cards(starting_decks):
    player1, player2 = starting_decks.split("\n\n")

    player1 = deque([int(card) for card in player1.split() if card.isdigit()])
    player2 = deque([int(card) for card in player2.split() if card.isdigit()])

    return player1, player2


def count_score(deck):
    return sum((len(deck) - i) * card for i, card in enumerate(deck))


def play_combat(deck1, deck2):
    while deck1 and deck2:
        c1, c2 = deck1.popleft(), deck2.popleft()

        if c1 > c2:
            deck1.extend([c1, c2])
        elif c2 > c1:
            deck2.extend([c2, c1])
    return deck1, deck2


def play_recursive_combat(deck1, deck2):
    # One deckhash per game
    deckhash = set()
    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in deckhash:
            break

        deckhash.add((tuple(deck1), tuple(deck2)))

        c1, c2 = deck1.popleft(), deck2.popleft()

        if c1 <= len(deck1) and c2 <= len(deck2):
            winner, __ = play_recursive_combat(
                deque(list(deck1)[:c1]), deque(list(deck2)[:c2])
            )
        else:
            winner = 1 if c1 > c2 else 2

        deck1.extend([c1, c2]) if winner == 1 else deck2.extend([c2, c1])

    # Will always put 1 as winner if 1 has cards left
    winner = 1 if deck1 else 2

    return winner, deck1 if winner == 1 else deck2


player1, player2 = play_combat(*parse_cards(test))
print(f"Part 1:\t{count_score(player1 if player1 else player2)}")

winner, winners_deck = play_recursive_combat(*parse_cards(test))
print(f"Part 2:\t{count_score(winners_deck)}")

