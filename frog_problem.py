import random
import matplotlib.pyplot as plt
import numpy

results = []


def do_jumps(starting_list, number_of_jumps):
    landing = random.choice(starting_list)
    jumps_no = number_of_jumps + 1
    if landing == starting_list[-1]:
        return jumps_no
    else:
        new_list = starting_list[starting_list.index(landing) + 1:]
        return do_jumps(new_list, jumps_no)


for i in range(1, 10):                    # specify the maximum number of lily pads
    pads_list = list(range(1, i+1))
    trials = []                             # blank list to contain trial results
    for x in range(10000):                   # specify the number of simulations
        trial = do_jumps(pads_list, 0)  # run do_jumps and plug in the number of lily pads (i)
        trials.append(trial)
    length_mean = sum(trials) / float(len(trials))
    results.append(length_mean)
    # if i.__mod__(10) == 0:
    #     print(str(i) + ' completed')

x = list(range(1, len(results)+1))
y = []
for i in x:
    temp = 0.0
    for z in range(1, i + 1):
        temp = temp + (1 / z)
    y.append(temp)

plt.plot(x, results, 'ro')
# plt.plot(x, numpy.log(x), 'bo')
plt.plot(x, y, 'bo')
plt.axis([0, len(results), 0, max(results)])
plt.xlabel('lily pads')
plt.show()
