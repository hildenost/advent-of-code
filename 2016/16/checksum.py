""" Advent of Code 2016. Dragon Checksum """


def checksum(data):
    checksum = ["1" if a == b else "0" for a, b in zip(data[::2], data[1::2])]
    while len(checksum) % 2 == 0:
        checksum = [
            "1" if a == b else "0" for a, b in zip(checksum[::2], checksum[1::2])
        ]
    return "".join(checksum)


def modified_dragon(string):
    return string + "0" + "".join("0" if c == "1" else "1" for c in string[::-1])


def find_checksum(state, length=272):
    while len(state) < length:
        state = modified_dragon(state)

    return checksum(state[:length])


print("Part 1:\t", find_checksum(state, length=272))
print("Part 2:\t", find_checksum(state, length=35651584))
