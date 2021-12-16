""" Advent of Code 2016. Day 20: Firewall Rules """

max_value = 4294967295

with open("input.txt") as f:
    blacklist = [tuple(int(d) for d in row.split("-")) for row in f.read().splitlines()]

pointer = 0 
min_ip = max_value
valid_ips = []
for start, end in sorted(blacklist):
    if pointer < start: 
        min_ip = min(min_ip, pointer)
        valid_ips.extend(range(pointer, start))

    pointer = max(pointer, end + 1)

print("Part 1:\t", min_ip)
print("Part 2:\t", len(valid_ips))
