""" Advent of Code 2021. Day 18: Snailfish """

import re

def split(number):
    t = re.search(r"\d\d+", number)
    if not t:
        return number

    t = int(t[0])
    new = f"[{t // 2},{t - t // 2}]"
    return re.sub(str(t), new, number, count=1)

def explode(pair):
    numbers = [int(n) for n in re.findall(r"(\d+)", pair)]

    n = 0
    i = 0
    lefts =[] 
    while i < len(pair):
        if len(lefts) > 4:
            #Time to explode
            if pair[i] == "[":
                # Ok lol soz, must step up one more
                lefts.append(pair[i])
                i += 1
                continue
            if n > 0:
                numbers[n-1] += numbers[n]
                j = i
                t = list(re.finditer(r"(\d+)", pair[:j]))[-1]
                delta = len(str(numbers[n-1])) - len(t[0])
                HEAD = pair[:t.start()] + str(numbers[n-1]) + pair[t.end():i-1]
            else:
                HEAD = pair[:i-1]

            start = i - 1
            while pair[i] != "]":
                i+=1
            i+= 1
            if n + 2 < len(numbers):
                numbers[n+2] += numbers[n+1]
                TAIL = re.sub(r"(\d+)", str(numbers[n+2]), pair[i:], count = 1)
            else:
                TAIL = pair[i:]

            pair = HEAD + "0" + TAIL
            numbers[n] = 0
            numbers.pop(n +1)
            return pair
        if pair[i] in "0123456789":
            n += 1
            while pair[i] in "0123456789":
                i += 1
        if pair[i] == "[":
            lefts.append(pair[i])
        if pair[i] == "]":
            lefts.pop()
        i += 1
    return pair


def reduce(number):
    new = explode(number)
    while new != number:
        number = new
        new = explode(number)
        if new == number:
            # Only if we haven't exploded, can we split
            new = split(number)
    return new

def add(a, b):
    return reduce(f"[{a},{b}]")

def mag(pair):
    if isinstance(pair, int):
        return int(pair)
    return 3*mag(pair[0]) + 2*mag(pair[1])

homework = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".splitlines()

with open("input.txt") as f:
    homework = f.read().splitlines()

import json
n = homework[0]
for o in homework[1:]:
    n = add(n, o)
n = json.loads(n)
print("Part 1:\t", mag(n))

from itertools import permutations
largest_snailfish = max(
        mag(json.loads(add(a, b)))
        for a, b in permutations(homework, 2)
)
print("Part 2:\t", largest_snailfish)

