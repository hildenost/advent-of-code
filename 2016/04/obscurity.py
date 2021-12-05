""" Advent of Code 2016. Day 4: Security Through Obscurity """
from collections import Counter

with open("input.txt") as f:
    rooms = f.read().splitlines()

def sort_common(common):
    return [c[0] for c in sorted(common, key=lambda x: (1/x[1], x[0]))][:5]

total = 0
valid_rooms = []
for room in rooms:
    checksum = room[-6:-1]
    sector_id = int(room[-10:-7])
    counts = Counter(room[:-10])
    del counts["-"]
    if checksum == "".join(sort_common(counts.most_common())):
        total += sector_id
        valid_rooms.append(room)
print("Part 1:\t", total)

alphabet = "abcdefghijklmnopqrstuvwxyz"
from itertools import cycle
def shift(letter, number):
    if letter == "-":
        return " "
    shifter = cycle(alphabet)
    s = next(shifter)
    while s != letter:
        s = next(shifter)
    for __ in range(number):
        letter = next(shifter) 
    return letter

for room in valid_rooms:
    sector_id = int(room[-10:-7])
    string = "".join(shift(r, sector_id) for r in room[:-10])
    if "north" in string:
        print("Part 2:\t", sector_id)

