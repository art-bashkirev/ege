from itertools import product

l = list(product("йняст", repeat=5))
for i in range(1, len(l) + 1):
    if l[i-1].count("т") == 0 and l[i-1].count("с") == 2:
        print(i, l[i-1])