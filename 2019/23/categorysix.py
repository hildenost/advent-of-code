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
        # Check for packets
        if not packets[address]:
            # IDLE
            output = nic.send(-1)
        else:
            # Packets! Yay!
            X, Y = packets[address].pop(0)
            nic.send(X)
            output = nic.send(Y)

        if output is None:
            # No packages output
            if not any(packets.values()):
                X, Y = NAT
                if prev == Y and prev is not None:
                    print("Part 2:\t", Y)
                    exit()
                prev = Y

                packets[0].append((X, Y))
                # Just breaking to start at 0 again
                # Saving some time
                break

            continue

        # Packages to send
        destination = output

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
        else:
            nic.send(-1)
