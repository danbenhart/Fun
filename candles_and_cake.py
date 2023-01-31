import random

trials = 10000000

successes = 0

for i in range(trials):
    candle_1 = random.random()
    candle_2 = random.random()
    cut = random.random()
    max_candle = max(candle_1, candle_2)
    min_candle = min(candle_1, candle_2)
    if min_candle < cut < max_candle:
        successes += 1

print(successes/trials)
