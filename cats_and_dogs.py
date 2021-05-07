import itertools

acceptable = 0

for p in itertools.product("cd", repeat=10):
    arr = ''.join(p)
    if 'cc' not in arr:
        acceptable += 1
        print(arr)

print(acceptable)