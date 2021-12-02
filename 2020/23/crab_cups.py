test = "389125467"
moves = 10

test = "362981754"
moves = 10_000_000


class Cup:
    def __init__(self, value):
        self.value = int(value)
        self.next = None

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        return self.value == other.value

    def __repr__(self):
        return f"{self.value}"


# The key to Part 2: easy retrieval of the destination value
all_cups = [None] * 1_000_000

curr = Cup(test[0])
all_cups[curr.value - 1] = curr
prev_cup = curr
for cup in test[1:]:
    new_cup = Cup(cup)
    all_cups[new_cup.value - 1] = new_cup
    if cup == "1":
        first = new_cup
    prev_cup.next = new_cup
    prev_cup = new_cup
new_cup.next = curr


for n in range(9 + 1, 1_000_000 + 1):
    new_cup = Cup(n)
    all_cups[new_cup.value - 1] = new_cup
    prev_cup.next = new_cup
    prev_cup = new_cup
new_cup.next = curr

min_value = 1
max_value = 1_000_000


def print_all(start):
    cups = [start]
    cup = start.next
    while cup != start:
        cups.append(cup)
        cup = cup.next

    print("cups:", " ".join(str(cup) for cup in cups))


for i in range(moves):
    pick_up = [curr.next, curr.next.next, curr.next.next.next]

    # Decide on destination value
    dest_value = curr.value - 1
    if dest_value < min_value:
        dest_value = max_value

    while dest_value in pick_up:
        dest_value -= 1
        if dest_value < min_value:
            dest_value = max_value

    # Find the destination cup
    cup = all_cups[dest_value - 1]

    # Move pointers
    # The current cup must now point to the cup immediately to the right of the
    # last cup in pick_up
    curr.next = pick_up[-1].next
    # The last cup in pick_up must point to the cup immediately to the right of the
    # destination_cup
    pick_up[-1].next = cup.next
    # The destination_cup must point to the first cup of pick_up
    cup.next = pick_up[0]

    # print_all(curr)

    curr = curr.next

# Find 1
cup = curr
while cup != 1:
    cup = cup.next

print(cup.next.value * cup.next.next.value)

