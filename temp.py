import numpy as np
import sympy
import itertools
import time


# def sigma_function(x, n, k):
#     #   compensates for duplicate copies of a factorial in the denominator of fraction
#     temp_factorial = np.math.factorial(k)
#     output = 1
#     temp_list = [x] * (n-1)
#     temp_list_list = [list(range(i + 1)) for i in temp_list]
#     # print('temp list', temp_list_list)
#     deductions = itertools.product(*temp_list_list)
#
#     while True:
#         deduction_combo = next(deductions, None)
#         # print('deduction', deduction_combo)
#         if deduction_combo is None:
#             break
#         else:
#             deduction = np.sum(deduction_combo)
#             print('64! /', k - deduction, '!')
#             # print('deduction sum:', deduction)
#             # print(k - deduction)
#             deduction_combo = list(deduction_combo)
#             deduction_combo.append(k)
#
#             output *= temp_factorial / np.product([np.math.factorial(i) for i in deduction_combo])
#
#     # for i in range(1, x * n + 1):
#     #     print('64! /', k-i, '!')
#     #     output *= temp_factorial/np.math.factorial(k-i)
#
#     return output

def sigma_function(x, n):
    #   compensates for duplicate copies of a factorial in the denominator of fraction
    output = 0

    for i in range(x + 1):
        output += 1/np.math.factorial(i)

    return output ** n


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

#   system for directly getting the correct answer for small multisets
#   will quickly hit memory limits for larger multisets
#
# perms = list(sympy.utilities.iterables.multiset_permutations('aabb_____', 5))
#
# print(len(perms))
#
# for perm in perms:
#     print(perm)


# choosing = 225
choosing = 64

multiset = []
for key in tiles:
    multiset.append(tiles[key][1])

# print(multiset)

# multiset = [2, 9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
multiset = [1, 2, 3, 3, 3]

# simplified version

simple_perm_count = 0

print('starting Simplified')
simple_combos = []
multiset_counts = []
multiset_temp = set(multiset)

for x in multiset_temp:
    multiset_counts.append([x, multiset.count(x)])

multiset = multiset_temp
a = [list(range(x + 1)) for x in multiset]
combos = itertools.product(*a)
print(multiset_counts)

null_list = []

start_time = time.time()

while True:
    next_combo = next(combos, None)
    if next_combo is None:
        break
    else:
        combo_list = list(next_combo)
        total_tiles = np.sum(combo_list)
        null_tiles = choosing - total_tiles

        # combo_list.append(null_tiles)
        # print(str(combo_list)[1:-1])
        # if combo_list not in simple_combos:
        simple_combos.append(combo_list)
        temp_simple_perm_count = (np.math.factorial(choosing) / np.product([np.math.factorial(x) for x in combo_list]))
        # for item in multiset_counts:
        #     # simple_perm_count *= sigma_function(item[0], item[1] - 1, choosing)
        #     x = item[0]
        #     n = item[1]
        #     if n > 1:
        #         # print(x, n, choosing)
        #         # print((x + 1) ** (n - 1))
        #         temp_simple_perm_count *= ((x + 1) ** (n - 1))
        #         temp_simple_perm_count /= sigma_function(x, n)

        simple_perm_count = temp_simple_perm_count
        # simple_perm_count += (np.math.factorial(choosing) / np.product([np.math.factorial(x) for x in combo_list]))

        # if null_tiles not in null_list:
        #     null_list.append(null_tiles)
        #     run_time = time.time() - start_time
            # print(total_tiles, run_time)
# print('Simple_Permutations: ', simple_perm_count)

for item in multiset_counts:
    # simple_perm_count *= sigma_function(item[0], item[1] - 1, choosing)
    x = item[0]
    n = item[1]
# if n > 1:
    # print(x, n, choosing)
    print((x + 1) ** (n - 1))
    # simple_perm_count = simple_perm_count * ((x + 1) ** (n - 1))
    simple_perm_count *= ((x + 1) ** (n - 1))
    simple_perm_count *= sigma_function(x, n - 1)
print('Simple_Permutations corrected: ', simple_perm_count)
# print(time.time() - start_time)
# for combo in simple_combos:
#     print(str(combo)[1:-1])

# full version

multiset = [1, 2, 3, 3, 3]

perm_count = 0

a = [list(range(x + 1)) for x in multiset]
combos = itertools.product(*a)
null_list = []
start_time = time.time()

all_combos = []
differences = []
while True:
    next_combo = next(combos, None)
    if next_combo is None:
        break
    else:

        # combo_list = list(next_combo)
        combo_list = list(next_combo)
        # total_tiles = np.sum(combo_list)
        # null_tiles = choosing - total_tiles
        # temp_combo = combo_list[:-2]
        # temp_combo.append(null_tiles)
        #
        # if temp_combo not in simple_combos:
        #     differences.append(temp_combo)
        #
        # combo_list.append(null_tiles)
        # print(str(combo_list)[1:-1])
        # if combo_list not in all_combos:
        all_combos.append(combo_list)
        # print(counts)
        perm_count += (np.math.factorial(choosing) / np.product([np.math.factorial(x) for x in combo_list]))

        # if null_tiles not in null_list:
        #     null_list.append(null_tiles)
        #     run_time = time.time() - start_time
            # print(total_tiles, run_time)

print('Permutations: ', perm_count)
# print(time.time() - start_time)
# for combo in all_combos:
#     print(str(combo)[1:-1])



# print('**********   Differences     **********')

# for combo in differences:
#     print(str(combo)[1:-1])

print(len(all_combos))

print('Difference: ', simple_perm_count / perm_count)

