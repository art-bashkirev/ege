from itertools import product

l = list(product("�����", repeat=5))
for i in range(1, len(l) + 1):
    if l[i-1].count("�") == 0 and l[i-1].count("�") == 2:
        print(i, l[i-1])