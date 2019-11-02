class Marble:
    def __init__(self, value, next_marble=None, prev_marble=None):
        self.value = value
        self.next_marble = next_marble if next_marble is not None else self
        self.prev_marble = prev_marble if prev_marble is not None else self


def insert(current_marble, new_marble):
    new_marble.next_marble = current_marble.next_marble.next_marble
    new_marble.prev_marble = current_marble.next_marble
    current_marble.next_marble.next_marble = new_marble
    new_marble.next_marble.prev_marble = new_marble

def remove_before(marble):
    marble.prev_marble = marble.prev_marble.prev_marble
    marble.prev_marble.next_marble = marble

def go_counter_clockwise(node, steps = 7):
    for i in range(steps):
        node = node.prev_marble
    return node

def marblescore(number_of_players, last_marble):
    players = [0]*number_of_players
    current_node = Marble(0)
    for i in range(1, last_marble+1):
        if i % 23 == 0:
            current_node = go_counter_clockwise(current_node)
            players[i % number_of_players] += i + current_node.value
            current_node = current_node.next_marble
            remove_before(current_node)
            continue

        new_node = Marble(i)
        insert(current_node, new_node)
        current_node = new_node
    return max(players)

assert 32 == marblescore(9, 25)
assert 8317 == marblescore(10, 1618)
assert 146373 == marblescore(13, 7999)
assert 2764 == marblescore(17, 1104)
assert 54718 == marblescore(21, 6111)
assert 37305 == marblescore(30, 5807)

print(marblescore(411, 7117000))
