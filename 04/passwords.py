from collections import Counter

min_pwd = 197487
max_pwd = 673251

def nonincreasing(numbers):
    return all(numbers[i-1] <= numbers[i] for i in range(1, 6))

total = sum(
    1
    for password in range(min_pwd, max_pwd+1)
    if 2 in Counter(str(password)).values() # PART 2
    #if len(set(str(password))) < 6 # PART 1
    and nonincreasing(str(password))
)

#total = 0
#for password in range(min_pwd, max_pwd+1):
#    pwd = str(password)
#    count_digits = Counter(pwd)
#
#    # The password need to have _exactly_ 2 digits that are
#    # similar. So, if there are no digits that occur
#    # exactly 2 times, the number is invalid.
#    if 2 not in count_digits.values():
#        continue
#
#    # The digits need to be non-increasing.
#    # This will also ensure that the 2 similar digits are
#    # indeed adjacent, because if they weren't,
#    # we would have decreasing digits.
#    if nonincreasing(pwd):
#        total += 1
#
print(total)
