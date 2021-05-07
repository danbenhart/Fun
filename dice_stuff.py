import numpy as np

rolls = 100000

# dice = [[4, 15], [6, 10], [10, 6], [12, 5]]
# results = []
#
# for die in dice:
#     temp = []
#     for i in range(rolls):
#         roll = np.random.randint(1, die[0], size=die[1])
#         total = np.sum(roll)
#         temp.append(total)
#     print([die[0], np.mean(temp), np.std(temp)])

dice = [6, 4]
results = 0
for i in range(rolls):
    if i%1000 == 0:
        print(i)
    temp = []
    for j in range(6):
        roll = np.random.randint(1, 7, size=4)
        top_three = sorted(roll)[1:]
        top_three_sum = np.sum(top_three)
        temp.append(top_three_sum)
    results += max(temp)

print(results/rolls)
