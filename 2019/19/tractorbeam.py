from input_prog import input_program
from intcode import run

def is_beam(x, y):
    drone = run(input_program + [0]*100)
    next(drone)
    drone.send(x)
    return drone.send(y)

### PART 1
print(sum(is_beam(x, y) for x in range(50) for y in range(50)))

### PART 2
def get_initial_point(X, Y):
    if not is_beam(X, Y):
        # If not a part of beam, iterate until beam is found
        while not is_beam(X, Y):
            X += 1
        # Then continue across beam
        while is_beam(X, Y):
            X += 1
        # And correcting the offset
        X -= 1
    return X, Y

def fit_square(X, Y, sidelength):
    # A square of sidelength sidelength can we can walk sidelength to the left
    # from the rightmost point on the beam,
    # AND we can walk down sidelength from there
    # This is the best solution because if the square did not fit
    # at y, then it can not fit at y+1 either unless x is changed
    return is_beam(X-sidelength+1, Y) and is_beam(X-sidelength+1, Y+sidelength-1)

def get_closest_corner(sidelength):
    # Starting out there somewhere
    X, Y = get_initial_point(0, sidelength)

    while not fit_square(X, Y, sidelength):
        # Update rightmost point on beam
        Y += 1
        while is_beam(X, Y):
            X += 1
        X -= 1
        # and continue
    return X-99, Y

x, y = get_closest_corner(100)
print(x*10000 + y)

