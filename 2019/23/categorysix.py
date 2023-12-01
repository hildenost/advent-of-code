""" Advent of Code 2019 Day 23: Category Six """
from intcode import run


# parse program
with open("input.txt") as f:
    program = [int(n) for n in f.read().split(",")]

from collections import defaultdict


def init_nic(i):
    prog = run(program + [0] * 100)
    next(prog)
    prog.send(i)
    return prog


# Initialize network
nics = [init_nic(i) for i in range(50)]

NAT = (0, 0)
prev = None
part1 = False
packets = defaultdict(list)

while True:
    for address, nic in enumerate(nics):
        # RECEIVE packets
        if packets[address]:
            # Packets! Yay!
            X, Y = packets[address].pop(0)
            nic.send(X)
            destination = nic.send(Y)
        else:
            # IDLE
            destination = nic.send(-1)

        if destination is None and not any(packets.values()):
            # The last package becoming idle
            # Meaning entire system is idle

            # Same Y value as last time
            if prev == NAT[1]:
                print("Part 2:\t", NAT[1])
                exit()

            # Send package from NAT to address 0
            packets[0].append(NAT)

            prev = NAT[1]

        # There are packages to send
        while destination is not None:
            X = next(nic)
            Y = next(nic)

            if destination == 255:
                if not part1:
                    print("Part 1:\t", Y)
                    part1 = True

                NAT = (X, Y)
            else:
                packets[destination].append((X, Y))

            destination = next(nic)
