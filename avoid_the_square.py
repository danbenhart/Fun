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
choosing = round(num_choices/2)

num_combs = np.math.factorial(num_choices) / (np.math.factorial(choosing) * np.math.factorial(num_choices - choosing))
print("checking all", str(int(num_combs)), "combinations")

coords = []

for i in range(grid_rows):
    for j in range(grid_columns):
        coords.append((i, j))


def create_blank_grid(rows, columns):
    grid = []
    i = 0
    j = 0
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            grid[i].append(0)
    return grid


#   takes a list of integers (used as indexes) and returns an array of the associated coordinate pairs
def indices_to_coords(indices):
    coord_set = []
    for i in indices:
        coord_set.append(coords[i])
    return np.array(coord_set)


working_solutions = []
i = 0
all_combos = itertools.combinations(range(0, num_choices), choosing)
for combo in all_combos:
    if i % 1000 == 0:
        print(i)
        print(combo)
    all_indices = list(range(0, num_choices))
    num_squares = 0
    sets_of_four = itertools.combinations(combo, 4)
    for foursome in sets_of_four:
        foursome_coords = indices_to_coords(foursome)
        # print(foursome_coords)
        #   use the spatial library to check all distances of the provided coordinates, return the unique ones
        distances = np.unique(distance.cdist(foursome_coords, foursome_coords))[1:]   # remove the leading 0
        # print(distances)
        # print(len(distances))
        if len(distances) == 2:
            num_squares += 1
            break
    if num_squares == 0:
        for index in combo:
            all_indices.remove(index)
        opponent_indices = tuple(all_indices)
        # print("opp indices", opponent_indices)
        opponent_sets_of_four = itertools.combinations(opponent_indices, 4)
        for opponent_foursome in opponent_sets_of_four:
            opponent_foursome_coords = indices_to_coords(opponent_foursome)
            #   use the spatial library to check all distances of the provided coordinates, return the unique ones
            distances = np.unique(distance.cdist(opponent_foursome_coords, opponent_foursome_coords))[1:]  # remove the leading 0
            # print(distances)
            # print(len(distances))
            # print("num squares = ", num_squares)
            if len(distances) == 2:
                # print(opponent_foursome_coords)
                num_squares += 1
                break
    if num_squares == 0:
        # print("working combo: ", str(combo))
        my_combo = indices_to_coords(combo)
        working_solutions.append(my_combo)
    i += 1

print("There are: ", str(len(working_solutions)), " working solutions")

for solution in working_solutions[10000]:
    # convert the list of points into a full grid
    solution_blank_grid = create_blank_grid(grid_rows, grid_columns)
    for point in solution:
        row = point[1]
        column = int(point[0])
        solution_blank_grid[row][column] = 1
    for row in solution_blank_grid:
        print(str(row)[1:-1])   # strip off the brackets, allows for easy copy-paste into Excel
    print("")


end_time = time.perf_counter()  # stop the timer
run_time = str(round(end_time - start_time, 2)) # round the run time to 2 decimals
print('Process took ' + run_time + ' seconds')
