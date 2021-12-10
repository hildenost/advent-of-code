""" Advent of Code 2021. Day 10: Syntax Scoring """

pairs = {"(": ")", "[":"]", "{": "}", "<":">"}

with open("input.txt") as f:
    lines = f.read().splitlines()

def check(line):
    lefts = []
    for p in line:
        if p in "{[(<":
            lefts.append(p)
        elif p in "}])>":
            l = lefts.pop()
            if pairs[l] != p:
                return p
    return "OK" 

score = { ")": 3, "]":57, "}": 1197, ">": 25137, "OK": 0}
print("Part 1:\t", sum(score[check(line)] for line in lines))


def autocomplete(line):
    lefts = []
    for p in line:
        if p in "{[(<":
            lefts.append(p)
        elif p in "}])>":
            l = lefts.pop()
    return [pairs[l] for l in reversed(lefts)]


score2 = {")":1, "]": 2, "}":  3, ">": 4}
def autoscore(parens):
    score = 0
    for p in parens:
        score = 5 * score + score2[p]
    return score

scores = sorted(
        autoscore(autocomplete(line))
        for line in lines
        if check(line) == "OK"
)

print("Part 2:\t", scores[len(scores) // 2])
        

