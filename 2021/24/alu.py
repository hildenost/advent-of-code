""" Advent of Code 2021. Day 24: Arithmetic Logic Unit """
program = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
""".splitlines()

with open("input.txt") as f:
    program = f.read().splitlines()

instructions = {
    "inp": lambda a, b: b,
    "add": lambda a, b: a + b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a // b,
    "mod": lambda a, b: a % b,
    "eql": lambda a, b: a == b
}

def run(program, stream, regs=None):
    if regs is None:
        regs = {k: 0 for k in "wxyz"}
    for i, line in enumerate(program):
        if len(line.split()) == 3:
            cmd, reg, arg = line.split()
            if arg[-1].isdigit():
                arg = int(arg)
            else:
                arg = regs[arg]
        else:
            cmd, reg = line.split()
            if not stream:
                return program[i:], regs
            arg = stream.pop(0) 
        regs[reg] = instructions[cmd](regs[reg], int(arg))
    return "", regs


"""
The number is composed of the following digits:
    abcdefghijklmn

To get z = 0, the following must hold: 
a + 3 = j   =>  a in [1,...,6], j in [4,...,9]
b + 4 = i   =>  b in [1,...,5], i in [5,...,9]
g + 8 = h   =>  g = 1, h = 9
e + 5 = f   =>  e in [1,2,3,4], f in [6,7,8,9]
d + 1 = c   =>  d in [1,...,8], c in [2,...,9]
k + 2 = n   =>  k in [1,...,7], n in [3,...,9]
m + 6 = l   =>  m in [1, 2, 3], l in [7, 8, 9]

I didn't solve this programmatically. I stepped through
the assembly code and always opted for the not equal-statement
to be False, as that would leave a much less complex z.
"""
# Digit limits
# digits = [(lower, upper),...]
digits = [
    (1, 6),
    (1, 5),
    (2, 9),
    (1, 8),
    (1, 4),
    (6, 9),
    (1, 1),
    (9, 9),
    (5, 9),
    (4, 9),
    (1, 7),
    (7, 9),
    (1, 3),
    (3, 9),
]

# Part 1 asked for the largest valid model number
print("Part 1:\t", "".join(str(max(d)) for d in digits))
# Part 2 asked for the smallest valid model number
print("Part 2:\t", "".join(str(min(d)) for d in digits))

"""
Below is my notes

1st number 
a in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 + 12 != a
# x is ALWAYS 1 since a < 12
z //= 1 
# z = 0
y = 25*x + 1

z *= y
# z = 0

y = x * (a + 7)
# x = 1 

z += y

# AFTER 1st:
#   z = a + 7
#

2nd number
b in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 + 11 != b
# x is ALWAYS 1 since b < 11

z //= 1
# z = a + 7

y = 25*x + 1
z *= y
z = 26 * (a + 7)
y = x * (b + 15)
z += y

# AFTER 2nd
z = 26 * (a + 7) + (b + 15)

3rd number
c in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 + 12 != c
# x is ALWAYS 1 since c < 12

z //= 1

y = 25*x + 1
z *= y
z = 26 * (26*(a + 7) + (b + 15))
y = x * (c + 2)
z += y

z = 26 * (26*(a + 7) + (b + 15)) + c + 2

4th number
d in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 - 3 != d
#z % 26 = c + 2
#c + 2 - 3 = c - 1
z //= 26

z = 26 * (a + 7) + (b + 15)

if c - 1 == d:
    # Let's assume this first
    z = 26 * (a + 7) + (b + 15)
else:
    # Don't even bother
    z *= 26
    z += (d + 15)
5th number
e in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 + 10 != e
# x is ALWAYS 1 since e < 10

z //= 1

z *= 26
z += (e + 14)

# z if assuming all ifs true
z = 26 * (26 * (a + 7) + (b+15)) + (e + 14) 

6th number
f in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 - 9 != f
#z % 26 = e + 14
#e + 14 - 9 = e + 5
z //= 26

if e + 5 == f:
    z = 26 * (a + 7) + (b + 15) 
else:
    z *= 26
    z += (f + 2)

7th number
g in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 + 10 != g
# x is ALWAYS 1 since g < 10

z //= 1

z *= 26
z += (g + 15)

z = 26* ( 26*(a + 7) + (b + 15)) + (g + 15)

8th number
h in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 - 7 != h
#z % 26 = g + 15
#g + 15 - 7 = g + 8 

z //= 26
if g + 8 == h:
    z = 26*(a +7) + (b + 15)
else:
    z *= 26
    z += (h + 1)

9th number
i in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 - 11 != i
#z % 26 = b + 15
#b + 15 - 11 = b + 4

z //= 26
if b + 4 == i:
    z = a + 7
else:
    z *= 26
    z += (i + 15)
10th number
j in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 - 4 != j
#z % 26 = a + 7
#a + 7 - 4 = a + 3

z //= 26
if a + 3 == j:
    z = 0
else:
    z *= 26
    z += (j + 15)

11th number
k in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 + 14 != k
# x is ALWAYS 1 since k < 14

z //= 1
# z = 0 if all True above

z *= 26
z += k + 12

z = k + 12

12th number
l in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 + 11 != l
# x is ALWAYS 1 since l < 11
z //= 1

z *= 26
z += l + 2

z = 26*(k + 12) + (l+2)

13th number
m in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 - 8 != m
# z % 26 = l + 2
# l + 2 - 8 = l - 6

z //= 26
if m + 6 == l:
    z = k + 12
else:
    z *= 26
    z += (m + 13)

14th number
n in [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = z % 26 - 10 != n
# z % 26 = k + 12
# k + 12 - 10 = k + 2
z //= 26
# z = 0 for all true

if k + 2 == n:
    z = 0
else:
    z *= 26
    z += (n + 13)

"""

