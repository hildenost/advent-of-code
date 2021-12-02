import numpy as np

def compute_power_levels(serial_number):
    rack_id = np.tile(np.arange(1, 301), (300,1)) + 10

    grid = rack_id * np.array([np.arange(1, 301)]).T
    grid += serial_number
    grid *= rack_id

    lowest_hundred =  (grid // 1000) * 10
    grid //= 100
    grid -= lowest_hundred
    grid -= 5

    return grid

def get_power_level(x, y, grid):
    return grid[y-1][x-1]

def test_power_levels(serial_number, expected, pos):
    grid = compute_power_levels(serial_number)
    assert expected == get_power_level(*pos, grid)

def sum_along_axis(matrix, indices, dims):
    sums = np.empty(dims)
    for i in range(dims[0]):
        c = np.r_[0, matrix[i].cumsum()][indices]
        sums[i] = c[:, 1] - c[:, 0]
    return sums


# Testing power level computations
test_data = [
    (8, 4, (3, 5)),
    (57, -5, (122, 79)),
    (39, 0, (217, 196)),
    (71, 4, (101, 153))
]

for test in test_data:
    test_power_levels(*test)

serial_number = 8

def get_max_indices(matrix):
    x, y = np.unravel_index(np.argmax(matrix, axis=None), matrix.shape)
    return x+1, y+1

def find_best_fuel_cells(serial_number):
    grid_size = 300

    grid = compute_power_levels(serial_number)

    max_sum = 0

    indices = np.arange(grid_size + 1)
    for j in range(1, 300):
        sum_size = grid_size - j + 1
        idcs = np.array([indices[:-j], indices[j:]]).T

        hor_sums = sum_along_axis(grid, idcs, (grid_size, sum_size))
        total_sums = sum_along_axis(hor_sums.T, idcs, (sum_size, sum_size))

        if total_sums.max() > max_sum:
            max_sum = total_sums.max()
            result = *get_max_indices(total_sums), j

    return result

serial_number = 5153
print(find_best_fuel_cells(serial_number))
