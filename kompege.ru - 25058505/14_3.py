def to7(n):
    s = []
    while n > 0:
        s = [n % 7] + s
        n //= 7
    return s

for x in range(2030, 0, -1):
    s = 7 ** 170 + 7 ** 100 - x
    if to7(s).count(0) == 71:
        print(x)
        print(to7(s))
        break
