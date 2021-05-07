number_range = 100


def new_triangle(a, b, c):
    if a == b == c:
        return 0
    # if sorted([a, b, c]) == [0, 7, 7]:
    #     return 0
    else:
        new_a = abs(a-b)
        new_b = abs(b-c)
        new_c = abs(a-c)
        if a + b + c == 14 and new_a + new_b + new_c == 14:
            print('success')
            return 1
        elif 0 in [a, b, c] and sorted([a, b, c])[1] == sorted([a, b, c])[2]:
            return 0
        else:
            return new_triangle(new_a, new_b, new_c)


for start_a in range(number_range):
    for start_b in range(start_a):
        for start_c in range(start_b):
            if start_a + start_b + start_c != 14:
                result = new_triangle(start_a, start_b, start_c)
                if result != 0:
                    print(start_a, start_b, start_c)
    print(start_a)
