import numpy as np
import pickle


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def save_obj(obj, output_dir, name):
    """
    :param obj: the object which will be pickled
    :param output_dir: the desired output directory
    :param name: the desired pickle file name
    :return:
    """
    output_filename = output_dir.joinpath(name + '.pkl')
    with open(output_filename, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    filename = name + '.pkl'
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
        return obj, type(obj)


def factors(x):
    factors_list = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return x, factors_list


def is_prime(x):
    assert x >= 2, 'number not large enough'
    for i in range(2, x):

        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (x % i) == 0:
            return False
    else:
        return True


def farey(x, n):
    a, b = 0, 1
    c, d = 1, 1
    while b <= n and d <= n:
        mediant = (a + c) / (b + d)
        if x == mediant:
            if b + d <= n:
                return a + c, b + d
            elif d > b:
                return c, d
            else:
                return a, b
        elif x > mediant:
            a, b = a + c, b + d
        else:
            c, d = a + c, b + d
    if b > n:
        return c, d
    else:
        return a, b


def create_blank_grid(rows, columns):
    grid = []
    i = 0
    j = 0
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            grid[i].append(0)
    return grid


def num_combs(k, n):    # returns the number of combinations when choosing k items from n choices
    return int(np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k)))


def prime_factorization(n):
    """Return the prime factorization of `n`.

    Parameters
    ----------
    n : int
        The number for which the prime factorization should be computed.

    Returns
    -------
    dict[int, int]
        List of tuples containing the prime factors and multiplicities of `n`.

    """
    prime_factors = {}

    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n /= i
            try:
                prime_factors[i] += 1
            except KeyError:
                prime_factors[i] = 1

    if n > 1:
        try:
            prime_factors[n] += 1
        except KeyError:
            prime_factors[n] = 1
    return prime_factors
