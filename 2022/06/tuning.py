""" Advent of Code 2022. Day 6: Tuning Trouble """

with open("input.txt") as f:
    msg = f.read().strip()

def find_signal(chars):
    for i in range(len(msg)):
        temp = msg[i:i+chars]
        if len(temp) == len(set(temp)):
            return i + chars

print("Part 1:\t", find_signal(chars=4))
print("Part 2:\t", find_signal(chars=14))
