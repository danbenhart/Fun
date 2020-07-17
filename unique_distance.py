#! python3

import numpy as np
import itertools
from scipy.spatial import distance
import copy
import time

start_time = time.perf_counter()    # start the timer to check the run time

#   set up the grid
grid_rows = 5
grid_columns = 5
num_choices = grid_rows * grid_columns
choosing = 13

#   generate a list of (X, Y) coordinate pairs
coords = []

for i in range(grid_rows):
    for j in range(grid_columns):
        coords.append((i, j))

#   determine how many combinations are going to be checked
num_combs = np.math.factorial(num_choices) / (np.math.factorial(choosing) * np.math.factorial(num_choices - choosing))
print("checking all", str(int(num_combs)), "combinations")


#   creates a grid filled with 0s, this is necessary when doing grid transformations
def create_blank_grid(rows, columns):
    grid = []
    i = 0
    j = 0
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            grid[i].append(0)
    return grid


#   takes a grid as input and returns the grid rotated 90 degrees clockwise
def rotate_cw(grid):
    rotated_grid_rows = len(grid)
    rotated_grid_columns = len(grid[0])

    cw_rotated_grid = create_blank_grid(rotated_grid_rows, rotated_grid_columns)

    for i in range(rotated_grid_rows):
        for j in range(rotated_grid_columns):
            new_row = j
            new_column = rotated_grid_rows - 1 - i
            cw_rotated_grid[new_row][new_column] = grid[i][j]

    return cw_rotated_grid


#   takes a grid as an input and returns all rotations for both chiralities (8 total, including the original)
def permutations(test_grid):
    single_rotation = rotate_cw(test_grid)
    double_rotation = rotate_cw(single_rotation)
    triple_rotation = rotate_cw(double_rotation)

    left_right = copy.deepcopy(test_grid)
    for lr_row in left_right:
        lr_row.reverse()

    single_rotation_lr = rotate_cw(left_right)
    double_rotation_lr = rotate_cw(single_rotation_lr)
    triple_rotation_lr = rotate_cw(double_rotation_lr)

    return single_rotation, double_rotation, triple_rotation, \
           left_right, single_rotation_lr, double_rotation_lr, triple_rotation_lr


#   takes a list of integers (used as indexes) and returns an array of the associated coordinate pairs
def indices_to_coords(indices):
    coord_set = []
    for i in indices:
        coord_set.append(coords[i])
    return np.array(coord_set)


working_solutions = []  # this will hold all the lists of points where all distances are unique
unique_working_solutions = []   # this will hold all solutions (in grid form) which are unique
perms_of_unique_working_solutions = []  # this will hold everything in unique_working_solutions plus all permutations

#   create a generator of all possible combinations of grid spaces
all_combos = itertools.combinations(range(0, num_choices), choosing)


for combo in all_combos:
    test = indices_to_coords(combo)
    #   use the spatial library to check all distances of the provided coordinates, return the unique ones
    distances = np.unique(distance.cdist(test, test))[1:]   # remove the leading 0

    # if all distances are unique, this is how many there are
    num_distances = ((choosing - 1)**2 + (choosing - 1)) / 2
    if len(distances) == num_distances:
        working_solutions.append(test)

for solution in working_solutions:
    # convert the list of points into a full grid
    solution_blank_grid = create_blank_grid(grid_rows, grid_columns)
    for point in solution:
        row = point[1]
        column = int(point[0])
        solution_blank_grid[row][column] = 1

    # check whether the solution is permutation of a previously checked solution
    if solution_blank_grid not in perms_of_unique_working_solutions:
        # if the solution is new
        # add it to the list of unique solutions and add it, plus all permutations to the all permutations list
        unique_working_solutions.append(solution_blank_grid)
        perms_of_unique_working_solutions.append(solution_blank_grid)
        perms = permutations(solution_blank_grid)
        for permutation in perms:
            perms_of_unique_working_solutions.append(permutation)

print(len(unique_working_solutions), ' unique solutions')

#   print the unique solutions for reference
for solution in unique_working_solutions:
    for row in solution:
        print(str(row)[1:-1])   # strip off the brackets, allows for easy copy-paste into Excel
    print("")

end_time = time.perf_counter()  # stop the timer
run_time = str(round(end_time - start_time, 2)) # round the run time to 2 decimals
print('Process took ' + run_time + ' seconds')
