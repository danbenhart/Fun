from dan_functions import is_prime

power = 3

for n in range(1, 100):

    # n = 19

    first_n_primes = []

    i = 2
    while len(first_n_primes) < n:
        if is_prime(i):
            first_n_primes.append(i)

        i += 1

    first_n_primes_squared = [x ** n for x in first_n_primes]
    sum_of_squares = sum(first_n_primes_squared)

    # print(first_n_primes)
    # print(first_n_primes_squared)
    #
    if sum_of_squares % n == 0:
        print(n)
        print(first_n_primes)
