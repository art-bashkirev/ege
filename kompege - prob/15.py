def d(n, m):
    return n % m == 0

b = [i for i in range(60, 80+1)]
for a in range(1, 100000):
    if all((d(x, a) or x not in b or (not d(x, 22))) is True for x in range(1, 1000000)):
        print(a)