from collections import Counter

min_pwd = 197487
max_pwd = 673251

pwds = (str(password) for password in range(min_pwd, max_pwd + 1))

total = sum(
    1
    for pwd in pwds
    # The digits need to be non-increasing.
    # This will also ensure that the 2 similar digits are
    # indeed adjacent, because if they weren't,
    # we would have decreasing digits.
    if list(pwd) == sorted(list(pwd))
    # PART 2:
    # The password need to have _exactly_ 2 digits
    # that are similar.
    and 2 in Counter(pwd).values() # PART 2
    # PART 1:
    # There need to be at least 1 digit
    # occuring at least 2 times.
    #and len(set(pwd)) < 6 # PART 1
)

print(total)
