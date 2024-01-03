""" Advent of Code 2023. Day 24: Never Tell Me The Odds """
import re
from itertools import combinations

with open("input.txt") as f:
    hails = f.read().splitlines()


hails = [[int(n) for n in re.findall(r"-?\d+", hail)] for hail in hails]


def intersect2d(a, b):
    """Find intersection of 2 vectors, but only in 2 dimensions.

    Returns None when no intersection is found, else the coordinates of the intersection.
    """
    xa, ya, __, vxa, vya, __ = a
    xb, yb, __, vxb, vyb, __ = b

    # is parallel:
    # denominator is 0
    denominator = vyb * vxa - vya * vxb

    if abs(denominator) > 0:
        s = ((ya - yb) * vxa + (xb - xa) * vya) / (vyb * vxa - vya * vxb)
        if s < 0:
            # Crossing happened in the past
            return None

        t = ((xb - xa) + vxb * s) / vxa
        if t < 0:
            # Crossing happened in the past
            return None

        x = xb + vxb * s
        y = yb + vyb * s
        return x, y


def count_within(minpos=200000000000000, maxpos=400000000000000):
    """Count the number of intersections within a given area."""
    count = 0
    for a, b in combinations(hails, 2):
        res = intersect2d(a, b)

        if res is not None:
            x, y = res
            count += minpos <= x <= maxpos and minpos <= y <= maxpos
    return count


print("Part 1:\t", count_within())

""" PART 2

The equations to be solved are:
    x + t * v = a + t * va
where   t is the timestep (unknown)
        x and v are position and velocity for the stone thrown (unknowns)
    and a and va are position and velocity for the hailstone (known)
All parameters should be integers, and t > 0 in addition.

Since only integer solutions are wanted, we are looking at a bunch of Diophantine
equations, which is the fancy name.

If we gather terms and solve for t, we get
    t = - (x-a) / (v-va) = - (y-ay) / (vy-vay) = - (z-az) / (vz-vaz)

Consequently, (v - va) perfectly divides (x-a), or in fancy notation: (v - va) | (x - a).

This means that the solution can be found separately for x, y, z as a system of
congruence equations on the form:
    x ≡ a   mod (v - va)
all per direction x, y, z.

The Chinese remainder theorem coupled with the extended Euclidean algorithm
for pairwise solving the congruences using Bézout's identity solves this.

However, there's a catch, as the modulus (v - va) essentially is unknown since
v is unknown.

Therefore, as a first step, we try to find pairs or more of congruences with equal modulus, in other words, 
finding hailstones of equal velocity in the same direction.

For two congruences of equal modulus m, we have:
    x ≡ a   mod m 
    x ≡ b   mod m 

    a ≡ b   mod m 
which gives
    a = b + k * m for some integers k that divides a - b.

Since m is v-va, we can find a limited suggestion for v which then can be used, trial and error, on the remaining
congruences.

So, lets' do that first, find the suggestions for the velocities of our stone in all three directions.

For my input, there were only 1 velocity suggestion per direction. There was also only 1 possible y position.
However, I decided to obfuscate my code a bit to solve in the case of multiple options, such as the test input.
"""


from math import gcd
from math import lcm
from functools import cache


# Caching this, it might give a speedup
@cache
def find_prime_divisors(n):
    divisors = []
    while n % 2 == 0:
        divisors.append(2)
        n //= 2
    while n % 3 == 0:
        divisors.append(3)
        n //= 3
    f = 5
    while f * f <= n:
        for k in (f, f + 2):
            while n % k == 0:
                divisors.append(k)
                n //= k
        f += 6
    if n > 1:
        divisors.append(n)
    return divisors


def find_divisors(n):
    """Find the integer divisors of n"""
    divisors = [1]
    if n == 1:
        return divisors

    prime_factors = find_prime_divisors(n)

    last_prime = 0
    factor = 0
    slice_len = 0
    for prime in prime_factors:
        if last_prime != prime:
            slice_len = len(divisors)
            factor = prime
        else:
            factor *= prime

        for i in range(slice_len):
            divisors.append(divisors[i] * factor)
        last_prime = prime

    return divisors


def extended_euclidean(a, b):
    """Solves the Bézout's identity ax + by = gcd(a, b)"""
    a, b = max(a, b), min(a, b)

    x = 1
    y = 0

    x1, y1, a1, b1 = 0, 1, a, b
    while b1:
        q = a1 // b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a1, b1 = b1, a1 - q * b1

    # x, y are the solution of Bézout's identity
    return x, y


def find_vs(a, b):
    """Find all valid xs so that (x - b) divides a,
    in other words, find x so that:
        a = k * (x - b)
    which gives that:
        x = a // k + b
    for all divisors k of a.
    Furthermore, since a // k is also a divisor of a,
    we simplify to:
        x = k + b
    where k might be positive or negative
    """
    divisors = find_divisors(a)

    xs = set()
    for k in divisors:
        xs.add(k + b)
        xs.add(-k + b)
    return xs


def find_v_options(xs, vx):
    vs = set()
    for a, b in combinations(xs, 2):
        # Find the valid velocity options given by this combination of hails of equal velocity
        # For some reason, making sure that we pass the positive difference, we end up with fewer options
        v = find_vs(abs(a - b), vx)

        if vs:
            # The velocity we search for must hold for all hails
            # That is, we only keep the vs that are in all combinations
            vs &= v
        else:
            vs = v

    return vs


def find_v(poses, vels):
    # Let us go through the list, searching for duplicates
    all_vs = set()
    for velocity in set(vels):
        if vels.count(velocity) > 1:
            # What are the corresponding xs?
            part_xs = [x for x, v in zip(poses, vels) if v == velocity]

            if all_vs:
                # The velocity we search for must hold for all hails
                # That is, we only keep the vs that are in all combinations
                all_vs &= find_v_options(part_xs, velocity)
            else:
                all_vs = find_v_options(part_xs, velocity)

    return all_vs


# Finding the valid velocities per direction
xs, ys, zs, vxs, vys, vzs = zip(*hails)
valid_vxs = find_v(xs, vxs)
valid_vys = find_v(ys, vys)
valid_vzs = find_v(zs, vzs)


def trivial(poses, velos, stone_velo):
    # If the stone velocity is equal to one of the hailstone's velocities,
    # this implies that the corresponding position of the hailstone is
    # the position of the stone.

    return [p for p, v in zip(poses, velos) if v == stone_velo]


def explore_options(poses, velos, v, xs, ys, zs, vxs, vys, vzs):
    options = trivial(poses, velos, v)
    for p in options:
        toptions = [
            (p - pos) // -(v - vel) if vel != v else 0 for pos, vel in zip(poses, velos)
        ]
        # Check if ts are valid
        if all(t >= 0 for t in toptions):
            # Checking all hails
            x = {ax + (vax - vx) * t for ax, vax, t in zip(xs, vxs, toptions) if t != 0}
            y = {ay + (vay - vy) * t for ay, vay, t in zip(ys, vys, toptions) if t != 0}
            z = {az + (vaz - vz) * t for az, vaz, t in zip(zs, vzs, toptions) if t != 0}
            if len(x) == 1 and len(y) == 1 and len(z) == 1:
                return x.pop(), y.pop(), z.pop()


from itertools import product

for vx, vy, vz in product(valid_vxs, valid_vys, valid_vzs):
    for ps, vs, v in [(xs, vxs, vx), (ys, vys, vy), (zs, vzs, vz)]:
        output = explore_options(ps, vs, v, xs, ys, zs, vxs, vys, vzs)
        if output is not None:
            # Solution, break
            answer = output
            break

print("Part 2:\t", sum(answer))
