import sympy
import numpy as np
import progressbar

liars = {}

widgets = [' [', progressbar.Timer(format='elapsed time: %(elapsed)s'), '] ', progressbar.Bar('*'),
           ' (', progressbar.AdaptiveETA(), ') ', ]

def prepare_n(n):
    k = n / 2
    if k % 2 != 0:
        return int(k)
    else:
        return int(prepare_n(k))


def examine_witness(a, n):
    d = prepare_n(n - 1)
    result = (a ** d % n == 1) or (a ** d % n == n-1)
    return result

cap = 10000
num_witnesses = np.math.factorial(cap)
bar = progressbar.ProgressBar(max_value=cap, widgets=widgets).start()

a = 0
for i in range(2, cap + 1):
    if i % 2 == 0:
        pass
    else:
        if not sympy.isprime(i):
            # print(i)
            for witness in range(2, i):
                result = examine_witness(witness, i)
                if result:
                    if str(witness) not in liars.keys():
                        liars[str(witness)] = []
                    liars[str(witness)].append(i)
    bar.update(i)

output_name = 'witness_numbers.csv'
file = open(output_name, 'w')

max = 0
offender = 0
for liar in liars:
    file.write(liar + ':')
    offenses = len(liars[liar])
    for offense in liars[liar]:
        file.write(str(offense) + ',')

    file.write('\n')
    if offenses > max:
        max = offenses
        offender = liar
file.close()
print(offender, liars[offender])
print(max)
