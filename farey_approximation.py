import numpy
import math

# start_decimal = 0.3369444340278278

max_int = 4000
start_a = 0
start_b = 1
start_c = 1
start_d = 1

base = 11
power = 6
divisor = 13

str_pi = str(numpy.pi)
max_chars = len(str_pi)


def chars_of_pi(base, power, divisor, test_num, test_denom):
    actual_decimal = base ** power / divisor
    approximation = actual_decimal / (test_num/test_denom)
    str_approx = str(approximation)

    i = 0
    while str_pi[i] == str_approx[i]:
        i += 1

    return i


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
    if (b > n):
        return c, d
    else:
        return a, b


# print(farey(start_decimal, max_int))

for base in range(1, 100):
    print(base)
    for power in range(1, 10):
        for divisor in range(1, 1000):
            decimal = base ** power / divisor
            decimal_div_pi = decimal / numpy.pi
            start, whole_number = math.modf(decimal_div_pi)
            # print(start, whole_number)
            numerator, denominator = farey(start, max_int)
            # print(numerator, denominator)
            final_numerator = denominator * whole_number + numerator
            # print(final_numerator, denominator)
            num_chars = chars_of_pi(base, power, divisor, final_numerator, denominator)
            if num_chars == max_chars:
                print(final_numerator, denominator, num_chars)


# decimal = base**power / divisor
# decimal_div_pi = decimal / numpy.pi
# start, whole_number = math.modf(decimal_div_pi)
# # print(start, whole_number)
# numerator, denominator = farey(start, max_int)
# # print(numerator, denominator)
# final_numerator = denominator * whole_number + numerator
# # print(final_numerator, denominator)
#
# # print(chars_of_pi(base, power, divisor, final_numerator, denominator))
