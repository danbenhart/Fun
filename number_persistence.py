import numpy as np
import random
import time

# def per(num, steps=0):
#     n_str = str(num)
#     if len(n_str) == 1:
#         return steps
#     else:
#         n_list = [int(j) for j in n_str]
#         result = 1
#         for j in n_list:
#             result *= j
#         # print(result)
#         steps += 1
#         return per(result, steps)


def per(num, steps=0):
    if len(num) == 1:
        return steps
    else:
        result = 1
        for j in num:
            result *= j
        # print(result)
        steps += 1
        result_list = [int(x) for x in str(result)]
        return per(result_list, steps)

# res = per(277777788888899)
# res = per(start)

# print(res)

# pattern = '2{0,1}3{0,1}4{0,1}6*7*8*9*'
# # print(pattern.fullmatch(str(277777788888899)))
# a = exrex.getone(pattern)
# print(a)
#
# num_len = 20000
#


num_digits = 8
start_num = [7] * num_digits
print(start_num)
for stage in range(num_digits - 1):

    for stage_89 in range(num_digits - (1 + 2 * stage)):
        # print(stage_89)
        change = [8] * (stage * 2) + [9]

        end_index = -(stage_89 + 1)
        start_index = end_index - len(change)
        # print(change, start_index, end_index)
        start_num[start_index: end_index] = change
        # per(start_num)
        print(start_num)

    for stage_87 in range(num_digits - (1 + 2 * stage)):
        # print(stage_87)
        change = [7] + [8] * ((stage * 2) + 1)

        start_index = stage_87
        end_index = start_index + len(change)
        # print(change, start_index, end_index)
        start_num[start_index: end_index] = change
        # per(start_num)
        print(start_num)

