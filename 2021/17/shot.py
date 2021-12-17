""" Advent of Code 2021. Day 17: Trick Shot """

target = (xmin, xmax, ymin, ymax)


def fire(vx, vy, getmax=False):
    ymax = 0
    x, y = (0, 0)
    while True:
        x, y = x + vx, y + vy
        vx += -1 if vx > 0 else 1 if vx < 0 else 0
        vy -= 1

        ymax = max(y, ymax)
        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            if getmax:
                return ymax
            return True
        if x > target[1] or y < target[2]:
            # passed target, abort
            return False


def fire_h(vx):
    x = 0
    while True:
        x += vx
        vx += -1 if vx > 0 else 1 if vx < 0 else 0

        if target[0] <= x <= target[1]:
            return True
        if x > target[1]:
            # passed target, abort
            return False
        if vx == 0:
            return False


def fire_y(vy):
    y = 0
    while True:
        y += vy
        vy -= 1

        if target[2] <= y <= target[3]:
            return True
        if y < target[2]:
            # passed target, abort
            return False


# Pre-screening velocities
vxs = [vx for vx in range(1000) if fire_h(vx)]
vys = [vy for vy in range(-1000, 1000) if fire_y(vy)]

maxy = max(fire(vx, vy, getmax=True) for vx in vxs for vy in vys if vy > 0)
print("Part 1:\t", maxy)

all_vs = {(vx, vy) for vx in vxs for vy in vys if fire(vx, vy)}
print("Part 2:\t", len(all_vs))
