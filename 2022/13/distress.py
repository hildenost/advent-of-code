""" Advent of Code 2022. Day 13: Distress Signal """
import json

with open("input.txt") as f:
    packetlist = f.read()

pairs = [p.split() for p in packetlist.split("\n\n")]


def traverse_list(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return None if a == b else a < b

    if isinstance(a, list) and isinstance(b, list):
        for m, n in zip(a, b):
            test = traverse_list(m, n)
            if test is not None:
                return test
        test = None if len(a) == len(b) else len(a) < len(b)
        if test is not None:
            return test
    else:
        # Else, we have an int and a list
        if isinstance(a, int):
            a = [a]
        if isinstance(b, int):
            b = [b]
        return traverse_list(a, b)

packets = []
total = 0
for k, (left, right) in enumerate(pairs):
    l = json.loads(left)
    r = json.loads(right)
    packets += [l, r]

    res = traverse_list(l, r)
    if res:
        total += k+1
print("Part 1:\t", total)

packets.append([[2]])
packets.append([[6]])

class Packet:
    def __init__(self, packets):
        self.packets = packets

    def __lt__(self, other):
        return traverse_list(self.packets, other.packets)

packets = sorted([Packet(p) for p in packets])
packets = [p.packets for p in packets]
a = packets.index([[2]])
b = packets.index([[6]])
print("Part 2:\t", (a+1)*(b+1))
