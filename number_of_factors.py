from dan_functions import prime_factorization
import matplotlib.pyplot as plt
import numpy as np

num_factors = []
ints = list(range(1, 1000))

for i in range(1, 1000):
    factors = prime_factorization(i)
    exponents = []
    for key in factors.keys():
        exponents.append(factors[key] + 1)
    divisors = np.product(exponents)
    num_factors.append(divisors)

plt.plot(ints, num_factors)
plt.show()

