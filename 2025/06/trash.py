""" Advent of Code 2025. Day 6: Trash Compactor"""

with open("input.txt") as f:
    *numbers, ops = f.read().splitlines()


numbers = [[int(n) for n in row.split()] for row in numbers]
ops = ops.split()
    
rowsum = sum(
    i+j+k+l if op == "+" else i*j*k*l
    for i, j, k, l, op in zip(*numbers, ops)
)
print("Part 1:\t", rowsum)

with open("input.txt") as f:
    *numbers, ops = f.read().splitlines()
cols = [[len(n) for n in row.split()] for row in numbers]
# Need to find max length per column
cols = [max(a, b, c, d) for a, b, c, d in zip(*cols)]
ops = ops.split()

rowsum = 0
idx = 0
for i in range(1000):
    colsize = cols[i]

    ns = []
    for row in numbers:
        ns.append(row[idx:idx+colsize])

    temp = 0 if ops[i] == "+" else 1
    for j in range(colsize):
        a = int(''.join(r[j] for r in ns))
        if ops[i] == "+":
            temp += a 
        elif ops[i] == "*":
            temp *= a
    rowsum += temp

    idx += cols[i] + 1
print("Part 2:\t", rowsum)

