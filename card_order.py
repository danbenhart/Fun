import itertools

all_combos = itertools.permutations([1, 2, 3, 4], 4)

for combo in all_combos:
    print(str(combo)[1:-1])
