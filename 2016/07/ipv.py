""" Advent of Code 2016. Day 7: Internet Protocol Version 7 """

ips = [
    "abba[mnop]qrst",
    "abcd[bddb]xyyx",
    "aaaa[qwer]tyui",
    "ioxxoj[asdfgh]zxcvbn"
]
import re

with open("input.txt") as f:
    ips = f.read().splitlines()


counter = 0
for ip in ips:
    matches = re.finditer(r"([a-z])([a-z])(\2)(\1)", ip)
    brackets = [(b.start(), b.end()-1) for b in re.finditer(r"\[.*?\]", ip)]

    valid = False
    for m in matches:
        # Ignoring any four letter combos
        if m[0][0] == m[0][1]:
            continue

        # If the match is between brackets, valid is False
        valid = not any(
            [True for start, end in brackets if start < m.start() < end]
        )
        
        if not valid:
            # if valid is False, just exit
            break

    counter += valid 
print("Part 1:\t", counter)

counter = 0
for ip in ips:
    i = 0
    abas = []
    babs = []
    is_bab = False
    while i < len(ip) - 2:
        if ip[i] == "[":
            is_bab = True
        if ip[i] == "]":
            is_bab = False
        if (ip[i] != ip[i+1]) and (ip[i] == ip[i+2]):
            if is_bab:
                # Inverting bab so it's easier to compare later
                babs.append(ip[i+1] + ip[i] + ip[i+1])
            else:
                abas.append(ip[i:i+3])
        i += 1
    counter += any(aba in babs for aba in abas)
print("Part 2:\t", counter)


