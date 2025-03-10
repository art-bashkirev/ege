a = lambda x: x + 1
b = lambda x: x + 4
c = lambda x: x * 2

from itertools import product

for s in range(1, 51):
    
    if a(s) < 51 or b(s) < 51 or c(s) < 51:
        for i in product([a, b, c], repeat=2):
            print(i[0](s) < 51 and i[1](s) >= 51)
            print(s)
        