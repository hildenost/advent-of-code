class Marble:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next if next is not None else self
        self.prev = prev if prev is not None else self

def insert(current, new):
    new.next = current.next.next
    new.prev = current.next
    current.next.next = new
    new.next.prev = new

def remove_before(marble):
    marble.prev = marble.prev.prev
    marble.prev.next = marble

def go_counter_clockwise(node):
    return node.prev.prev.prev.prev.prev.prev.prev

def marblescore(number_of_players, last):
    players = [0]*number_of_players
    current_node = Marble(0)
    for i in range(1, last+1):
        if i % 23 == 0:
            current_node = go_counter_clockwise(current_node)
            players[i % number_of_players] += i + current_node.value
            current_node = current_node.next
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

print("Part 1:\t", marblescore(411, 71170))
print("Part 2:\t", marblescore(411, 7117000))
