from dan_functions import *
import itertools
import numpy as np
import time

cap = 20
group_size = 3

for test_value in range(2, cap):
    start_time = time.time()
    max_value = test_value

    num_permutations = np.math.factorial(max_value)

    all_prime_combos = 0

    all_combos = itertools.permutations(range(1, max_value + 1), max_value)
    for combo in all_combos:
        # print(combo)
        non_prime_groups = 0
        for i in range(max_value - (group_size - 1)):
            group = combo[i:i + group_size]
            if is_prime(sum(group)):
                pass
            else:
                non_prime_groups = 1
                break
        if non_prime_groups == 0:
            all_prime_combos += 1
    end_time = time.time()
    run_time = end_time - start_time
    print('for ', test_value, ' there are ', all_prime_combos, ' prime combos and took', run_time, ' to check')
