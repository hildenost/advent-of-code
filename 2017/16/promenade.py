""" Advent of Code 2017. Day 16: Permutation Promenade """

programs = list("abcdefghijklmnop")

with open("input.txt") as f:
    dance_moves = f.read().split(",")

def dance(dance_moves, progs="abcdefghijklmnop"):
    programs = list(progs)
    for move in dance_moves:
        if move[0] == "s":
            i = int(move[1:])
            if i > len(programs):
                print("Wups")
                exit()
            programs = programs[-i:] + programs[:-i]
        elif move[0] == "x":
            a, b = move[1:].split("/")
            programs[int(a)], programs[int(b)] = programs[int(b)], programs[int(a)]
        elif move[0] == "p":
            a, b = move[1:].split("/")
            a = programs.index(a)
            b = programs.index(b)
            programs[a], programs[b] = programs[b], programs[a]
    return "".join(programs)

print("Part 1:\t", dance(dance_moves))


# When we at starting condition,
# it will repeat forever

# First, generate all positions
prev = "abcdefghijklmnop"
dances = [prev]
while True:
    prev = dance(dance_moves, prev)
    if prev == "abcdefghijklmnop":
        break
    dances.append(prev)

# Then look up the equivalent dance
n = 1000000000 % len(dances)
print("Part 2:\t", dances[n])
    


        


