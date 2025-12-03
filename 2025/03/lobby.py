""" Advent of code 2025. Day 3: Lobby """

with open("input.txt") as f:
    batteries = f.read().splitlines()

def get_joltage(batteries, n=2):
    return sum(int(find_largest(n, battery)) for battery in batteries)

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


print("Part 1:\t", get_joltage(batteries,n=2))
print("Part 2:\t", get_joltage(batteries,n=12))
