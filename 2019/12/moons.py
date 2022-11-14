import numpy as np

def update_positions(moons, velocities):
    return moons + velocities

def update_velocities(moons, velocities):
    i = np.array([0, 0, 0, 1, 1, 2])
    j = np.array([1, 2, 3, 2, 3, 3])
    diff = np.sign(moons[i] - moons[j])

    np.subtract.at(velocities, i, diff)
    np.add.at(velocities, j, diff)

    return velocities

def compute_total_energy(moons, velocities):
    return (
        abs(moons).sum(axis=1) *
        abs(velocities).sum(axis=1)
    ).sum()

def run_steps(moons, velocities, timesteps):
    for __ in range(timesteps):
        velocities = update_velocities(moons, velocities)
        moons = update_positions(moons, velocities)
    return compute_total_energy(moons, velocities)

#### PART 1
moons = np.array([
    [-8, -9, -7],
    [-5, 2, -1],
    [11, 8, -14],
    [1, -4, -11]
])
velos = np.zeros_like(moons)
print(run_steps(moons, velos, 1000))

#### PART 2
def run(moons, velocities):
    moons_0 = moons.copy()
    velos_0 = velocities.copy()
    t = 0
    times = [0, 0, 0]
    while not all(t > 0 for t in times):
        t += 1
        velocities = update_velocities(moons, velocities)
        moons = update_positions(moons, velocities)

        if (
            np.array_equal(moons[:, 0], moons_0[:, 0])
            and np.array_equal(velocities[:, 0], velos_0[:, 0])
            and times[0] == 0
        ):
            times[0] = t
        if (
            np.array_equal(moons[:, 1], moons_0[:, 1])
            and np.array_equal(velocities[:, 1], velos_0[:, 1])
            and times[1] == 0
        ):
            times[1] = t
        if (
            np.array_equal(moons[:, 2], moons_0[:, 2])
            and np.array_equal(velocities[:, 2], velos_0[:, 2])
            and times[2] == 0
        ):
            times[2] = t

    print(times)
    # Need to factor them
    # Did it manually


moons = np.array([[-8, -9, -7], [-5, 2, -1], [11, 8, -14], [1, -4, -11]])
velos = np.zeros_like(moons)
run(moons, velos)

#### TESTS
def test_first_example():
    moons_1 = np.array([
        [-1, 0, 2],
        [2, -10, -7],
        [4, -8, 8],
        [3, 5, -1]
    ])
    velos = np.zeros_like(moons_1)
    assert 179 == run_steps(moons_1, velos, 10)

def test_second_example():
    moons_2 = np.array([
        [-8, -10, 0],
        [5, 5, 10],
        [2, -7, 3],
        [9, -8, -3]
    ])
    velos = np.zeros_like(moons_2)
    assert 1940 == run_steps(moons_2, velos, 100)
