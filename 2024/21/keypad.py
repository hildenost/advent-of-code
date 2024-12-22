""" Advent of Code 2024. Day 21: Keypad Conundrum """

from itertools import permutations

A = "A"


class KeyPad:
    @property
    def current(self):
        return self[(self.i, self.j)]

    def __getitem__(self, key):
        return self.pad.get(key)

    def push(self):
        print(self.current)


class NumericKeyPad(KeyPad):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+ ^
        | 0 | A | | j
        +---+---+ |
            i <---+
    """

    pad = {
        (0, 0): "A",
        (1, 0): "0",
        (2, 1): "1",
        (1, 1): "2",
        (0, 1): "3",
        (2, 2): "4",
        (1, 2): "5",
        (0, 2): "6",
        (2, 3): "7",
        (1, 3): "8",
        (0, 3): "9",
    }

    def __init__(self):
        self.i = 0
        self.j = 0


class DirectionalKeyPad(KeyPad):
    """
        +---+---+
        | ^ | A |
    +---+---+---+ ^ j
    | < | v | > | |
    +---+---+---+ |
            i <---+

    """

    pad = {(0, 0): ">", (1, 0): "v", (2, 0): "<", (0, 1): "A", (1, 1): "^"}

    def __init__(self, child=None):
        self.i = 0
        self.j = 1

        if child is None:
            self.child = NumericKeyPad()
        else:
            self.child = child

    def move(self, m):
        if m == "<":
            self.child.i += 1
        elif m == ">":
            self.child.i -= 1
        elif m == "^":
            self.child.j += 1
        elif m == "v":
            self.child.j -= 1
        elif m == "A":
            self.child.push()

        return self.child.current


dirc = DirectionalKeyPad()

dirc2 = DirectionalKeyPad(child=dirc)
dirc3 = DirectionalKeyPad(child=dirc2)


# print(dirc.child.i, dirc.child.j, dirc.child.current)
# for move in "<A^A>^^AvvvA":
#    # print("MOVE ", move)
#    dirc.move(move)
#    # print(dirc.child.i, dirc.child.j, dirc.child.current)
#
# print(dirc2.child.i, dirc2.child.j, dirc2.child.current)
# for move in "v<<A>>^A<A>AvA<^AA>A<vAAA>^A":
#    # print("MOVE ", move)
#    dirc2.move(move)
#    # print(dirc2.child.i, dirc2.child.j, dirc2.child.current)
#    # input()
# Dirpad
pad = {(0, 0): ">", (1, 0): "v", (2, 0): "<", (0, 1): "A", (1, 1): "^"}
pad = {v: k for k, v in pad.items()}
inv_pad = {(0, 0): ">", (1, 0): "v", (2, 0): "<", (0, 1): "A", (1, 1): "^"}
# Numpad
numpad = {
    (0, 0): "A",
    (1, 0): "0",
    (2, 1): "1",
    (1, 1): "2",
    (0, 1): "3",
    (2, 2): "4",
    (1, 2): "5",
    (0, 2): "6",
    (2, 3): "7",
    (1, 3): "8",
    (0, 3): "9",
}
numpad = {v: k for k, v in numpad.items()}
inv_numpad = {
    (0, 0): "A",
    (1, 0): "0",
    (2, 1): "1",
    (1, 1): "2",
    (0, 1): "3",
    (2, 2): "4",
    (1, 2): "5",
    (0, 2): "6",
    (2, 3): "7",
    (1, 3): "8",
    (0, 3): "9",
}
# Let's do it in reverse
code = "029A"
print(numpad)

ms = {(-1, 0): ">", (1, 0): "<", (0, 1): "^", (0, -1): "v"}

poscode = [numpad[c] for c in "A" + code]
print(poscode)

# LETS FIND THE OPTIONAL MOVES
from collections import defaultdict


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
        nummoves[(a, b)] = "^" * ((b - a) // 3)
        nummoves[(b, a)] = "v" * ((b - a) // 3)
    elif 1 <= a <= 3 and 1 <= b <= 3:
        # Horizontal
        nummoves[(a, b)] = ">" * (b - a)
        nummoves[(b, a)] = "<" * (b - a)
    elif 4 <= a <= 6 and 4 <= b <= 6:
        # Horizontal
        nummoves[(a, b)] = ">" * (b - a)
        nummoves[(b, a)] = "<" * (b - a)
    elif 7 <= a <= 9 and 7 <= b <= 9:
        # Horizontal
        nummoves[(a, b)] = ">" * (b - a)
        nummoves[(b, a)] = "<" * (b - a)
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

print(len(nummoves))
dirmoves = {
    (A, "^"): ["<"],
    ("^", A): [">"],
    (A, ">"): ["v"],
    (">", A): ["^"],
    (A, "v"): ["v<"],
    ("v", A): ["<v"],
    (A, "<"): ["<v<", "v<<"],
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

exit()

moves = defaultdict()
for a, b in zip(poscode, poscode[1:]):
    di, dj = b[0] - a[0], b[1] - a[1]

    if (di, dj) in moves:
        print("BEEN")
        print(moves[(di, dj)])
        input()

    if dj == 0:
        # Horizontal movement only
        # One option only
        n = abs(di)
        moves[(di, dj)] = [n * ms[(di // n, dj)]]
    elif di == 0:
        # Vertical movement only
        # One option only
        n = abs(dj)
        moves[(di, dj)] = [n * ms[(di, dj // n)]]
    else:
        # The "tricky" part
        # Dummy solution first
        # assume di 0
        n = abs(dj)
        moves[(0, dj)] = [n * ms[(0, dj // n)]]
        # assume dj 0
        n = abs(di)
        moves[(di, 0)] = [n * ms[(di // n, 0)]]

        # Then find options
        tmp = moves[(0, dj)] + moves[(di, 0)]

        # We assume the best option is moving same direction
        # as many times in a row as possible
        # moves[(di, dj)] = set(permutations(tmp))
        moves[(di, dj)] = [tmp]


print(moves)

"""
        +---+---+
        | ^ | A |
    +---+---+---+ ^ j
    | < | v | > | |
    +---+---+---+ |
            i <---+

    """

# Best options has to be multiple same pressures in a row


def diffs(a, b):
    return b[0] - a[0], b[1] - a[1]


def get_moves(a, b):
    # Special care needed for cases where
    # going from or to col 2
    # As that's where the gap is

    di, dj = diffs(a, b)

    is_horizontal = not dj
    is_vertical = not di

    is_col_2 = 2 in [a[0], b[0]]
    print("IS COL 2 ??? ", is_col_2)

    if (di, dj) in moves:
        print("BEEN")
        return moves[(di, dj)]

    if dj == 0:
        # Horizontal movement only
        # One option only
        n = abs(di)
        m = n * ms[(di // n, dj)]
    elif di == 0:
        # Vertical movement only
        # One option only
        n = abs(dj)
        m = n * ms[(di, dj // n)]
    elif is_col_2:
        print("IS COL 2!")
        input()
        # assume di 0
        n = abs(dj)
        vert = n * ms[(0, dj // n)]
        # assume dj 0
        n = abs(di)
        hori = n * ms[(di // n, 0)]
        if di < 0:
            # Going RIGHT
            # Best move is horizontal first
            # We (wrongly?) assume

            print("GOING RIGHT: ", hori + vert)
            m = hori + vert
        else:
            # Going LEFT
            # Best move is vertical first
            # We (wrongly?) assume
            print("GOING LEFT: ", vert + hori)
            m = vert + hori
        input()
    else:
        # The "tricky" part
        # Dummy solution first
        # assume di 0
        n = abs(dj)
        vert = n * ms[(0, dj // n)]
        # assume dj 0
        n = abs(di)
        hori = n * ms[(di // n, 0)]

        # Then find options
        tmp = vert + hori

        # We assume the best option is moving same direction
        # as many times in a row as possible
        # moves[(di, dj)] = set(permutations(tmp))
        m = tmp
    return m


# FOR DIR, SPECIAL CASES are ^A to different col and row
def dfs(orders, level=1):
    if level == 3:
        print("DONE\t\t\t", orders)
        # input()
        return orders
    print(orders, level)
    poscode = [pad[c] for c in "A" + orders]
    print(poscode)

    word = ""
    for a, b in zip(poscode, poscode[1:]):
        print(orders, ":\t", a, b, diffs(a, b))
        di, dj = diffs(a, b)
        is_horizontal = not dj
        is_vertical = not di
        is_up_or_A = (inv_pad[a] in "^A") or (inv_pad[b] in "^A")
        print(f"{is_horizontal=}")
        print(f"{is_vertical=}")
        print(f"{is_up_or_A=}")
        if not (is_horizontal or is_vertical) and is_up_or_A:
            print("SPECIAL TREATMENT")
            print("Up or down?\t", dj)
            print("Left or right?\t", di)
            if dj < 0:
                # Going down
                # Best move is vertical first
                # We (wrongly?) assume
                m = "v"

                n = abs(di)
                m += n * ms[(di // n, 0)] + "A"
                print("GOING DOWN: ", m)
            else:
                # Going up
                # Best move is horizontal first
                # We (wrongly?) assume
                n = abs(di)
                m = n * ms[(di // n, 0)]
                m += "^" + "A"
                print("GOING UP: ", m)
        else:
            if di == 0 and dj == 0:
                # Same button
                m = "A"
            elif dj == 0:
                # Horizontal movement only
                # One option only
                n = abs(di)
                m = n * ms[(di // n, dj)] + "A"
            elif di == 0:
                # Vertical movement only
                # One option only
                n = abs(dj)
                m = n * ms[(di, dj // n)] + A
            else:
                # The "tricky" part
                # Dummy solution first
                # Should probably minimize number of <'s as they require most
                # steps from A
                # assume di 0
                n = abs(dj)
                m = n * ms[(0, dj // n)]
                # assume dj 0
                n = abs(di)
                m += n * ms[(di // n, 0)] + A

        print("WHEN HERE, WE HAVE FOUND MOVES: ", m)
        # input()

        word += dfs(m, level + 1)

    print("WORD: \t", word)
    # input()
    return word


# SPECIAL CASES are 1 4 7 to different col and row
print(numpad)

ms = {(-1, 0): ">", (1, 0): "<", (0, 1): "^", (0, -1): "v"}


cmd = ""
for a, b in zip(poscode, poscode[1:]):
    print(a, b, diffs(a, b))
    options = moves[diffs(a, b)]
    print(options)
    for option in options:
        print(dfs("".join(option) + "A"))
        cmd += dfs("".join(option) + "A")


print(code)
print(cmd)
print(len(cmd), int(code[:-1]))
print(len(cmd) * int(code[:-1]))
print()
print()

code = "980A"
poscode = [numpad[c] for c in "A" + code]
print(poscode)
cmd = ""
for a, b in zip(poscode, poscode[1:]):
    print(a, b, diffs(a, b))
    options = get_moves(a, b)
    print(options)
    for option in options:
        print(dfs("".join(option) + "A"))
        cmd += dfs("".join(option) + "A")


print(code)
print(cmd)
print(len(cmd), int(code[:-1]))
print(len(cmd) * int(code[:-1]))
print()
print()

code = "179A"
poscode = [numpad[c] for c in "A" + code]
print(code)
print(poscode)
cmd = ""
for a, b in zip(poscode, poscode[1:]):
    print(a, b, diffs(a, b))
    options = get_moves(a, b)
    print(options)
    for option in options:
        print(dfs("".join(option) + "A"))
        cmd += dfs("".join(option) + "A")


print(cmd)
print(len(cmd), int(code[:-1]))
print(len(cmd) * int(code[:-1]))
