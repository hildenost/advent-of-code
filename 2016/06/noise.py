""" Advent of Code 2016. Day 6: Signals and Noise """

message = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
""".splitlines()

with open("input.txt") as f:
    message = f.read().splitlines()

columns = [[line[i] for line in message] for i in range(len(message[0]))]

from collections import Counter

# The most common character per column
word = "".join(Counter(c).most_common(1)[0][0] for c in columns)
print("Part 1:\t", word)

# The least common character per column
word = "".join(Counter(c).most_common()[-1][0] for c in columns)
print("Part 2:\t", word)



