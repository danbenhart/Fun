def print_factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors


num = 1
while True:
    print(num)
    factors_of_num = print_factors(num)
    if len(factors_of_num) == 64:
        print('number: ', num)
        for factor in factors_of_num:
            print(factor)
        break
    else:
        num += 1
