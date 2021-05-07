def balance(day_1, day_2, a, b, days):
    c = a + b
    a = b
    b = c

    if b == 1000000:
        return True, days
    if b > 1000000:
        if day_1 % 1000 == 0 and day_2 % 1000 == 0:
            print(day_1, day_2)
        # print('this does not work after' + str(days) + str(a) + ", " + str(b))
        return False, days
    else:
        days += 1
        return balance(day_1, day_2, a, b, days)


current_max = [0, 0, 0]

for i in range(1, 1000):
    for k in range(1, 1000):
        works, days = balance(i, k, i, k, 2)
        if works:
            if days > current_max[2]:
                current_max[2] = days
                current_max[0] = i
                current_max[1] = k
                print(i, k, days)

print(current_max)
