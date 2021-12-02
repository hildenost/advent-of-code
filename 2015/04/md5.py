import hashlib

key = "yzbqklnj"


def find_lowest_key(string, n=5):
    number = 0
    while True:
        test = hashlib.md5((string + str(number)).encode()).hexdigest()

        if test.startswith("0" * n):
            return number
        number += 1


print(find_lowest_key(key, n=5))
print(find_lowest_key(key, n=6))
