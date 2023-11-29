""" Advent of Code 2019. Day 22: Slam Shuffle """
with open("input.txt") as f:
    shuffles = f.read().splitlines()


# This holds per shuffle
#   p = a * p0 + b
# where p0 is initial position and p is position at end of shuffle


def shuffle(shuffles, m):
    a = 1
    b = 0
    for shuffle in shuffles[::-1]:
        first, *__, last = shuffle.split()
        if last == "stack":
            b += a * (-1)
            a *= -1
        elif first == "deal":
            a *= int(last)
        else:
            b += a * (-int(last))
        b %= m
        a %= m
    return a, b


deck = 10007
a, b = shuffle(shuffles, deck)
print("Part 1:\t", (a * 2019 + b) % deck)

deck = 119315717514047
a, b = shuffle(shuffles, deck)
k = 101741582076661


def is_odd(n):
    return n % 2 == 1


def F(r, n, m):
    """Computes the sum of the geometric series 1 + r + r^2 + ... + r^n (mod m)"""
    if n == 0:
        return 1

    if is_odd(n):
        return ((1 + r) % m * F((r * r) % m, ((n - 1) // 2) % m, m)) % m

    return (1 + (r + r * r) % m * F((r * r) % m, ((n - 2) // 2) % m, m)) % m


r = pow(a, deck - 2, mod=deck)
geomsum = F(r, k - 1, deck)

# p0 = a**(m-2) * ( (a**((m-2)*(k-1)) *pk - b * sum)
# p0 = r * (r**(k-1) * pk - b * geomsum)
# p0 = r**k * pk - r*b*geomsum

r_powk = pow(r, k, mod=deck)
constant = (r * b * geomsum) % deck
pk = 2020

print("Part 2:\t", (r_powk * pk - constant) % deck)
