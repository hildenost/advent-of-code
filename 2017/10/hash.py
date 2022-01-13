""" Advent of Code 2017. Day 10: Knot Hash """

lst = [0, 1, 2, 3, 4]
lengths = [3, 4, 1, 5]


def twist(lst, lengths, p=0, skip=0):
    for length in lengths:
        if p + length > len(lst):
            sublist = (lst[p:] + lst[: length - len(lst[p:])])[::-1]

            lst[p:] = sublist[: len(lst[p:])]
            lst[: length - len(lst[p:])] = sublist[len(lst[p:]) :]
        else:
            sublist = lst[p : p + length][::-1]
            lst[p : p + length] = sublist

        p += length + skip
        p %= len(lst)

        skip += 1
    return lst, p, skip


def sparsehash(lengths):
    lst = list(range(256))
    p = 0
    skip = 0
    for __ in range(64):
        lst, p, skip = twist(lst, lengths, p, skip)
    return lst


def densehash(lst):
    numbers = []
    for i in range(16):
        block = lst[16 * i : 16 * (i + 1)]
        number = block[0]
        for n in block[1:]:
            number ^= n
        numbers.append(number)
    return numbers


def to_hex(numbers):
    return "".join(f"{number:02x}" for number in numbers)


def knothash(lengths):
    additional = [17, 31, 73, 47, 23]
    lengths = [ord(l) for l in lengths] + additional
    return to_hex(densehash(sparsehash(lengths)))


lst, p, skip = twist(list(range(256)), lengths)

if __name__ == "__main__":
    print("Part 1:\t", lst[0] * lst[1])
    lengths = ",".join(str(l) for l in lengths)
    print("Part 2:\t", knothash(lengths))

