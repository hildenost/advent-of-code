from collections import defaultdict
from itertools import permutations

A = "A"

# LETS ENUMERATE ALL THE MOVES

nummoves = {
    (A, 0): ["<"],
    (0, A): [">"],
    (A, 3): ["^"],
    (3, A): ["v"],
    (A, 6): ["^^"],
    (6, A): ["vv"],
    (A, 9): ["^^^"],
    (9, A): ["vvv"],
    (A, 2): ["<^", "^<"],
    (2, A): ["v>", ">v"],
}
nummoves[(A, 1)] = [m + "<" for m in nummoves[(A, 2)]]
nummoves[(1, A)] = [">" + m for m in nummoves[(2, A)]]

nummoves[(A, 5)] = [m + "^" for m in nummoves[(A, 2)]]
nummoves[(5, A)] = ["v" + m for m in nummoves[(2, A)]]

nummoves[(A, 5)].extend([m + "<" for m in nummoves[(A, 6)]])
nummoves[(5, A)].extend([">" + m for m in nummoves[(6, A)]])

nummoves[(A, 8)] = [m + "^" for m in nummoves[(A, 5)]]
nummoves[(8, A)] = ["v" + m for m in nummoves[(5, A)]]

nummoves[(A, 8)].extend([m + "<" for m in nummoves[(A, 9)]])
nummoves[(8, A)].extend([">" + m for m in nummoves[(9, A)]])

nummoves[(A, 4)] = [m + "^" for m in nummoves[(A, 1)]]
nummoves[(4, A)] = ["v" + m for m in nummoves[(1, A)]]

nummoves[(A, 4)].extend([m + "<" for m in nummoves[(A, 5)]])
nummoves[(4, A)].extend([">" + m for m in nummoves[(5, A)]])

nummoves[(A, 7)] = [m + "^" for m in nummoves[(A, 4)]]
nummoves[(7, A)] = ["v" + m for m in nummoves[(4, A)]]

nummoves[(A, 7)].extend([m + "<" for m in nummoves[(A, 8)]])
nummoves[(7, A)].extend([">" + m for m in nummoves[(8, A)]])
from itertools import combinations

# SPECIAL CASES 1 4 7
for a, b in combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2):
    if a == 0:
        if b in [2, 5, 8]:
            n = (b - a - 2) // 3 + 1
            # Vertical
            nummoves[(a, b)] = ["^" * n]
            nummoves[(b, a)] = ["v" * n]
        elif b == 3:
            nummoves[(a, b)] = ["^>", ">^"]
            nummoves[(b, a)] = ["v<", "<v"]
        elif b in [6, 9]:
            nummoves[(a, b)] = [m + "^" for m in nummoves[(a, b - 3)]]
            nummoves[(b, a)] = ["v" + m for m in nummoves[(b - 3, a)]]

            nummoves[(a, b)].extend([m + ">" for m in nummoves[(a, b - 1)]])
            nummoves[(b, a)].extend(["<" + m for m in nummoves[(b - 1, a)]])
        elif b == 1:
            nummoves[(a, b)] = ["^<"]
            nummoves[(b, a)] = [">v"]
        elif b in [4, 7]:
            n = (b + 1 - a - 2) // 3 + 1
            # Vertical

            nummoves[(a, b)] = [m + "^" for m in nummoves[(a, b - 3)]]
            nummoves[(b, a)] = ["v" + m for m in nummoves[(b - 3, a)]]

            nummoves[(a, b)].append("^" * n + "<")
            nummoves[(b, a)].append(">" + "v" * n)
    elif not abs(a - b) % 3 and 0 not in [a, b]:
        # Vertical
        nummoves[(a, b)] = ["^" * ((b - a) // 3)]
        nummoves[(b, a)] = ["v" * ((b - a) // 3)]
    elif 1 <= a <= 3 and 1 <= b <= 3:
        # Horizontal
        nummoves[(a, b)] = [">" * (b - a)]
        nummoves[(b, a)] = ["<" * (b - a)]
    elif 4 <= a <= 6 and 4 <= b <= 6:
        # Horizontal
        nummoves[(a, b)] = [">" * (b - a)]
        nummoves[(b, a)] = ["<" * (b - a)]
    elif 7 <= a <= 9 and 7 <= b <= 9:
        # Horizontal
        nummoves[(a, b)] = [">" * (b - a)]
        nummoves[(b, a)] = ["<" * (b - a)]
    elif not (b - a) % 4 and a != 3:
        # Diagonal
        n = (b - a) // 4
        nummoves[(a, b)] = list(set("".join(p) for p in permutations("^>" * n, n * 2)))
        nummoves[(b, a)] = list(set("".join(p) for p in permutations("v<" * n, n * 2)))
    elif not (b - a) % 2:
        # Anti-diagonal
        n = (b - a) // 2
        nummoves[(a, b)] = list(set("".join(p) for p in permutations("^<" * n, n * 2)))
        nummoves[(b, a)] = list(set("".join(p) for p in permutations("v>" * n, n * 2)))
    # The only remaining are chess knight moves
    elif a in [1, 4] and b in [6, 9]:
        nummoves[(a, b)] = list(set("".join(p) for p in permutations(">>^", 3)))
        nummoves[(b, a)] = list(set("".join(p) for p in permutations("v<<", 3)))
    elif a in [1, 2] and b in [8, 9]:
        nummoves[(a, b)] = list(set("".join(p) for p in permutations(">^^", 3)))
        nummoves[(b, a)] = list(set("".join(p) for p in permutations("vv<", 3)))
    elif a in [2, 3] and b in [7, 8]:
        nummoves[(a, b)] = list(set("".join(p) for p in permutations("<^^", 3)))
        nummoves[(b, a)] = list(set("".join(p) for p in permutations("vv>", 3)))
    else:
        nummoves[(a, b)] = list(set("".join(p) for p in permutations("<<^", 3)))
        nummoves[(b, a)] = list(set("".join(p) for p in permutations("v>>", 3)))

dirmoves = {
    (A, "^"): ["<"],
    ("^", A): [">"],
    (A, ">"): ["v"],
    (">", A): ["^"],
    (A, "v"): ["<v", "v<"],
    ("v", A): ["^>", ">^"],
    (A, "<"): ["v<<", "<v<"],
    ("<", A): [">>^", ">^>"],
    ("^", "<"): ["v<"],
    ("<", "^"): [">^"],
    ("^", "v"): ["v"],
    ("v", "^"): ["^"],
    ("^", ">"): ["v>", ">v"],
    (">", "^"): ["^<", "<^"],
    (">", "<"): ["<<"],
    ("<", ">"): [">>"],
    (">", "v"): ["<"],
    ("v", ">"): [">"],
    ("<", "v"): [">"],
    ("v", "<"): ["<"],
}
