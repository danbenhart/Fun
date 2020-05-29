import numpy as np
import itertools
from scipy.spatial import distance
import copy


test = [[1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1]]


def create_blank_grid(rows, columns):
    grid = []
    i = 0
    j = 0
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            grid[i].append(0)
    return grid


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


def permutations(test_grid):
    single_rotation = rotate_cw(test_grid)
    double_rotation = rotate_cw(single_rotation)
    triple_rotation = rotate_cw(double_rotation)

    test_grid_rows = len(test_grid)

    upside_down = copy.deepcopy(test_grid)
    for i in range(test_grid_rows):
        upside_down[i] = test_grid[test_grid_rows - 1 - i]

    single_rotation_ud = rotate_cw(upside_down)
    double_rotation_ud = rotate_cw(single_rotation_ud)
    triple_rotation_ud = rotate_cw(double_rotation_ud)

    left_right = copy.deepcopy(test_grid)
    for lr_row in left_right:
        lr_row.reverse()

    single_rotation_lr = rotate_cw(left_right)
    double_rotation_lr = rotate_cw(single_rotation_lr)
    triple_rotation_lr = rotate_cw(double_rotation_lr)

    print(left_right == double_rotation_ud)

    return single_rotation, double_rotation, triple_rotation, upside_down, single_rotation_ud, double_rotation_ud, \
        triple_rotation_ud, left_right, single_rotation_lr, double_rotation_lr, triple_rotation_lr


all_perms = []
unique_perms = []

perms = permutations(test)

for perm in perms:
    all_perms.append(perm)
    if perm not in unique_perms:
        unique_perms.append(perm)

print(len(all_perms))
print(len(unique_perms))

