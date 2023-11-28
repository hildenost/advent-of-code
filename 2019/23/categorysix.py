""" Advent of Code 2019 Day 23: Category Six """
from intcode import run


# parse program
with open("input.txt") as f:
    program = [int(n) for n in f.read().split(",")]


# prog = run(program + [0] * 100)
#
# print(next(prog))
# print(prog.send(0))
# print(prog.send(-1))

from collections import defaultdict

packets = defaultdict(list)


def process(nic, address):
    # Check for packets
    if not packets[address]:
        # IDLE
        got_packets = False
        output = nic.send(-1)
    else:
        # Packets! Yay!
        got_packets = True
        while packets[address]:
            X, Y = packets[address].pop(0)
            nic.send(X)
            output = nic.send(Y)

    if output is None:
        # No packages output
        return nic, not got_packets

    # Packages to send
    destination = output

    while destination is not None:
        X = next(nic)
        Y = next(nic)
        print(f"From {address} send to {destination} package {X=}, {Y=}")

        if destination == 255:
            # print("Part 1:\t", Y)
            print("Writing to 255 from ", address, X, Y)
            print(packets[destination])
            packets[destination] = (X, Y)
            print(packets[destination])
        else:
            packets[destination].append((X, Y))

        destination = next(nic)
    else:
        nic.send(-1)

    return nic, False


def init_nic(i):
    prog = run(program + [0] * 100)
    next(prog)
    prog.send(i)
    return prog


# Initialize network
nics = [init_nic(i) for i in range(50)]

prev = None

# Start network
while True:
    nics, is_idle = zip(*[process(nic, i) for i, nic in enumerate(nics)])

    if all(is_idle):
        print("ALL IDLE")
        X, Y = packets[255]
        print("SENDING ", Y, " TO 0")

        if prev == Y and prev is not None:
            print("TWICE IN ROW!")
            print(prev, Y)
            exit()

        prev = Y

        packets[0].append((X, Y))
