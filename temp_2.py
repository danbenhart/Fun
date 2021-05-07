import numpy as np
import sympy
import itertools
import time
test_string = 'mississippi'

perms = 0
for i in range(len(test_string) + 1):
    perms += len(list(sympy.utilities.iterables.multiset_permutations(test_string, i)))

print(perms)