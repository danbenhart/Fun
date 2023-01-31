from math import gcd
from matplotlib import pyplot as plt
from itertools import count, filterfalse


def coprime2(a, b):
    return gcd(a, b) == 1


terms = [1, 2, 3]

seq_length = 1000

for term in range(3, seq_length):
    candidates = filterfalse(set(terms).__contains__, count(1))
    test_candidate = next(candidates)
    while not coprime2(terms[term - 1], test_candidate) or coprime2(terms[term - 2], test_candidate):
        test_candidate = next(candidates)
    terms.append(test_candidate)

plt.plot(list(range(seq_length)), terms)
plt.show()
