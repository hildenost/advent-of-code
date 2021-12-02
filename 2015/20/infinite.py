""" Advent of Code 2015. Day 20: Infinite Elces and Infinite Houses """
import math
# part 2
# elf 1 delivers until house 50
# elf 2 -> house 100
# elf 3 -> house 150
# elf 4 -> house 200

def factorisation(number):
  roof = math.floor(math.sqrt(number)) + 1
  factors = {1}
  for n in range(2, roof):
    if number % n == 0:
      factors.update({n, number // n})

  factors.update({number})
  return sum(factors) * 10

def finite_fact(number):
  if number == 0:
    return 0
  roof = math.floor(math.sqrt(number)) + 1
  factors = set() 
  for n in range(1, roof):
    if number % n == 0:
      factors.update({n, number // n})

  factors = {f for f in factors if f*50 >= number}
  return sum(factors)*11

threshold = 29000000


def solve(limit, part=1):
  func = factorisation if part == 1 else finite_fact
  house_number = 0 if part == 1 else 665280
  test = 1
  while test < limit:
    house_number += 1
    test = func(house_number) 
    print(house_number, " => ", test, " presents")

  return house_number


#print("PART 1:\t", part1(threshold))
def sieve(limit):
  A = [True for __ in range(limit)]

  A[0] = False
  A[1] = False

  for i in range(2, math.ceil(math.sqrt(limit))):
    if A[i]:
      for j in range(i*i, limit, i):
        A[j] = False
  return [i for i, a in enumerate(A) if a]

#print(sieve(threshold))


# Should use Sieve of Eratosthenes
print("PART 2:\t", solve(threshold, part=2))
