""" Advent of Code 2015. Day 1!: Corporate Policy """
password = "vzbxkghb"

def straight(n):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  return {alphabet[i:i+n] for i in range(len(alphabet)- n + 1)}

def is_valid(p):
  criteria_one = any(p[i:i+3] in straight(3) for i in range(len(p)-3+1))
  criteria_two = not any(c in p for c in "iol")
  criteria_three = sum(c * 2 in p for c in alphabet) >= 2
  return criteria_one and criteria_two and criteria_three

def increase_forbidden(p):
  loc_i = p.find("i")
  loc_o = p.find("o")
  loc_l = p.find("l")

  illegal = min([loc if loc != -1 else len(p) for loc in [loc_i, loc_o, loc_l]])
  if illegal == len(p):
    # No illegal letters, exiting
    return p

  return p[:illegal] + chr(ord(p[illegal]) + 1) + "a"*(len(p) - illegal -1)

def increase_by_one(p):
  new_password = p
  for k, char in enumerate(p[::-1]):
    pos = len(p) - k - 1
    if char != "z":
      return new_password[:pos] + chr(ord(char) + 1) + new_password[pos+1:]
    new_password = new_password[:pos] + "a" + new_password[pos+1:]
  return new_password

def next_password(p):
  if is_valid(p):
    p = increase_by_one(p)

  while not is_valid(p):
    new = increase_forbidden(p)
    p = increase_by_one(p) if new == p else new
  return p


password = next_password(password)
print("Part 1: ", password)

password = next_password(password)
print("Part 2: ", password)





