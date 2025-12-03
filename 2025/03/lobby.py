""" Advent of code 2025. Day 3: Lobby """

with open("input.txt") as f:
    batteries = f.read().splitlines()

joltage = 0
for battery in batteries:
    for first_digit in "987654321":
        idx = battery.find(first_digit)
        if idx in [-1, 99]:
            # digit not found or digit in last position
            continue
        second_digit = max(battery[idx+1:])
        joltage += int(first_digit + second_digit)
        break
print("Part 1:\t", joltage)

def find_largest(n, b):
    if n == 1:
        return max(b) 

    idx = b.find(max(b))

    # Always select the leftmost
    # except when there are 
    # not enough batteries left to the right
    remaining = len(b[idx:])
    if n <= remaining:
        # Business as usual, keep selecting the max
        # and searching to the right
        return max(b) + find_largest(n-1, b[idx+1:])

    # Now, here we must do stuff
    # find_largest between prev and new and tag the remainder
    # to the right
    return find_largest(n-remaining,b[:idx]) + b[idx:]


joltage = sum(int(find_largest(12, battery)) for battery in batteries)
print("Part 2:\t", joltage)
