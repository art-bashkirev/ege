def R(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    
    d -= set([1, x])
    return sum(d)

c = 0
n = 500001
while c < 5:
    r = R(n)
    if (r % 10 == 9):
        print(n, r)
        c += 1
    n += 1