""" Advent of Code 2017. Day 17: Spinlock """

pos = 0
step = 369
buffr = [0]
for i in range(1, 2018):
    pos = (pos+step)%i + 1
    buffr = buffr[:pos] + [i] + buffr[pos:]
print("Part 1:\t", buffr[pos+1])

pos = 0
step = 369
answer = 0
for i in range(1, 50000001):
    pos = (pos+step)%i + 1
    if pos == 1:
        answer = i
print("Part 2:\t", answer)
