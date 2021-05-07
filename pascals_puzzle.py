odds = 0
all_nums = 0


def generate_nth_row(n):
    # row = [1]
    prev = 1
    row_odds = 1

    for i in range(1, n + 1):
        curr = (prev * (n - i + 1)) // i
        # if curr % 2 == 1:
        #     row_odds += 1
        row_odds += curr % 2
        # row.append(curr)
        prev = curr

    # print(row)
    # print(row_odds, n + 1)
    return row_odds


for num in range(10000):
    a = generate_nth_row(num)
    odds += a
    all_nums += num + 1

    print([num, a, odds, all_nums, float(odds/all_nums) * 100])

# print(float(odds/all_nums) * 100)
