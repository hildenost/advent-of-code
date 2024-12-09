""" Advent of Code 2024. Day 9: Disk Fragmenter """
import timeit

start_time = timeit.default_timer()
with open("input.txt") as f:
    diskmap = f.read().strip()


def checksum(filesystem):
    return sum(
        i * int(block) for i, block in enumerate(filesystem) if block is not None
    )


example = "2333133121414131402"
example1 = "12345"


def maxID(diskmap):
    return len(diskmap) // 2


# diskmap = example

blocks = [int(block) for block in diskmap[::2]]
spaces = [int(space) for space in diskmap[1::2]]


# left = 0
# right = maxID(diskmap)
#
# res = [left] * blocks[left]
# blocks[left] = 0
# for space in spaces:
#    n = space
#    while n and left < right:
#        # Place so many blocks we can
#        if blocks[right] < n:
#            # Place all
#            res.extend([right] * blocks[right])
#            # Remove them
#            n -= blocks[right]
#            blocks[right] = 0
#            # And move to next
#            right -= 1
#        else:
#            # Place a few
#            res.extend([right] * n)
#            # Remove them
#            blocks[right] -= n
#            n = 0
#    if not n:
#        # No space, adding the next fileblock before moving on
#        left += 1
#        res.extend([left] * blocks[left])
#        blocks[left] = 0
# print(checksum(res))


# Skal vi lage et nøstehelvete?
# [[0 0], [None, None, None], [1, 1, 1]]?
# Og ha et kart over lengdene?

disk = [blocks[0] * [0]]
for i, (space, block) in enumerate(zip(spaces, blocks[1:]), 1):
    if space:
        disk.append([None] * space)
    disk.append([i] * block)

sizes = [len(n) for n in disk]
addresses = {n[0]: i for i, n in enumerate(disk) if n[0] is not None}

# Starting from the back
p = maxID(diskmap)

while p >= 0:
    # print("Disk ID:\t", p)
    # Located disk ID
    a = addresses[p]
    selected = disk[a]

    # Searching available space
    for i in range(a):
        if disk[i] and disk[i][0] is not None:
            continue

        if sizes[a] <= sizes[i]:
            if sizes[a] == sizes[i]:
                disk = (
                    disk[:i]
                    + [selected]
                    + disk[i + 1 : a]
                    + [[None] * sizes[a]]
                    + disk[a + 1 :]
                )

                sizes = [len(n) for n in disk]
            else:
                disk = (
                    disk[:i]
                    + [selected]
                    + [[None] * (sizes[i] - sizes[a])]
                    + disk[i + 1 : a]
                    + [[None] * sizes[a]]
                    + disk[a + 1 :]
                )
                sizes = [len(n) for n in disk]
            addresses = {n[0]: i for i, n in enumerate(disk) if n[0] is not None}
            # update block id
            p -= 1
            break
    else:
        # Did not move
        # update block id
        p -= 1


def flatten(disk):
    return [b for block in disk for b in block]


# print(disk)
print(checksum(flatten(disk)))
print(timeit.default_timer() - start_time)
