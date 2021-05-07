import numpy as np
import sympy
import itertools
import time


def sigma_function(x, no_instances):
    #   compensates for duplicate copies of a factorial in the denominator of fraction
    output = 0
    for a in range(x + 1):
        output += 1/np.math.factorial(a)

    return output ** no_instances


tiles = {
    '_': [0, 2],
    'a': [1, 9],
    'b': [3, 2],
    'c': [3, 2],
    'd': [2, 4],
    'e': [1, 12],
    'f': [4, 2],
    'g': [2, 3],
    'h': [4, 2],
    'i': [1, 9],
    'j': [8, 1],
    'k': [5, 1],
    'l': [1, 4],
    'm': [3, 2],
    'n': [1, 6],
    'o': [1, 8],
    'p': [3, 2],
    'q': [10, 1],
    'r': [1, 6],
    's': [1, 4],
    't': [1, 6],
    'u': [1, 4],
    'v': [4, 2],
    'w': [4, 2],
    'x': [8, 1],
    'y': [4, 2],
    'z': [10, 1],
}


test_string = 'mississippi'


# choosing = 225
choosing = 11

test_string_set = set(test_string)
multiset = [test_string.count(x) for x in test_string_set]

# multiset = []
# for key in tiles:
#     multiset.append(tiles[key][1])

# print(multiset)

# multiset = [2, 9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]


# region simplified version
# this version attempts to simplify the full algorithm by taking advantage of the number of duplicates in the multiset

simple_multiset = multiset.copy()
# print(simple_multiset)

simple_perm_count = 0

print('starting Simplified')
all_simple_combos = []
simple_multiset_counts = []
simple_multiset_temp = set(simple_multiset)

for x in simple_multiset_temp:
    simple_multiset_counts.append([x, simple_multiset.count(x)])

simple_multiset = simple_multiset_temp
simple_multiset_combos = [list(range(x + 1)) for x in simple_multiset]
simple_combos = itertools.product(*simple_multiset_combos)
print(simple_multiset_counts)

null_list = []

start_time = time.time()

while True:
    next_combo = next(simple_combos, None)
    if next_combo is None:
        break
    else:
        combo_list = list(next_combo)
        total_tiles = np.sum(combo_list)
        null_tiles = choosing - total_tiles
        combo_list.append(null_tiles)
        # print(str(combo_list)[1:-1])
        # if combo_list not in simple_combos:
        all_simple_combos.append(combo_list)
        simple_perm_count += (np.math.factorial(np.sum(combo_list)) /
                              np.product([np.math.factorial(x) for x in combo_list]))

        # if null_tiles not in null_list:
        #     null_list.append(null_tiles)
        #     run_time = time.time() - start_time
        #     print(total_tiles, run_time)
print('Simple_Permutations: ', simple_perm_count)
# print('Simple Combos: ', len(simple_combos))

for item in simple_multiset_counts:
    x = item[0]
    n = item[1]
    # if n > 1:
    # print(x, n, choosing)
    # print((x + 1) ** (n - 1))
    # simple_perm_count *= ((x + 1) ** (n - 1))
    simple_perm_count *= sigma_function(x, n - 1)
print('Simple_Permutations corrected: ', simple_perm_count)
# print(time.time() - start_time)
# for combo in simple_combos:
#     print(str(combo)[1:-1])

# endregion


# region full version
# this algorithm correctly generates all possible r-permutations

perm_count = 0

full_multiset_combos = [list(range(x + 1)) for x in multiset]
full_combos = itertools.product(*full_multiset_combos)
null_list = []
start_time = time.time()

all_full_combos = []
differences = []
while True:
    next_combo = next(full_combos, None)
    if next_combo is None:
        break
    else:
        combo_list = list(next_combo)
        total_tiles = np.sum(combo_list)

        # null_tiles = choosing - total_tiles
        # combo_list.append(null_tiles)
        # print(str(combo_list)[1:-1])
        # if combo_list not in all_combos:
        all_full_combos.append(combo_list)
        perm_count += (np.math.factorial(np.sum(combo_list)) / np.product([np.math.factorial(x) for x in combo_list]))

        # if null_tiles not in null_list:
        #     null_list.append(null_tiles)
        #     run_time = time.time() - start_time
        #     print(total_tiles, run_time)

print('Permutations: ', perm_count)
# print(time.time() - start_time)
# for combo in all_combos:
#     print(str(combo)[1:-1])

# endregion

# print('**********   Differences     **********')
# for combo in differences:
#     print(str(combo)[1:-1])

# print('All Combos: ', len(all_combos))

print('Difference: ', simple_perm_count / perm_count)

#   functions to get the correct answer for small multisets
#   will quickly hit memory limits for larger multisets
#


# include spaces
perms = len(list(sympy.utilities.iterables.multiset_permutations(test_string + '-' *
                                                                 (len(test_string)), choosing)))
print('True Perms with Spaces: ', perms)

# no spaces
perms = 0
for i in range(len(test_string) + 1):
    perms += len(list(sympy.utilities.iterables.multiset_permutations(test_string, i)))

print('True Perms without Spaces: ', perms)
