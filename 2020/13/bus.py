#test = """\
#939
#7,13,x,x,59,x,31,19
#"""
test = """\
939
1789,37,47,1889
"""

with open("13/input.txt") as f:
    test = f.read()


def parse_input(notes):
    timestamp, buses = notes.splitlines()
    buses = {int(b): i for i, b in enumerate(buses.split(",")) if b != "x"}
    return int(timestamp), buses


ts, bs = parse_input(test)

# Solving part 2 by the Chinese Remainder Theorem
product_of_all = 1
for b in bs:
    product_of_all *= b

ns = {b: product_of_all // b for b in bs}

answer = 0
for b, n in ns.items():
    # Finding the modular multiplicative inverse
    # But since all b's are prime numbers
    # we can use the shortcut that is Fermat's Little Theorem
    y = n ** (b - 2)
    answer += -bs[b] * y * n
print(answer % product_of_all)


exit()
earliest = (bs[0], bs[0] - (ts % bs[0]))
for b in bs:
    diff = b - ts % b
    if diff < earliest[1]:
        earliest = (b, diff)

print(earliest[0]*earliest[1])
