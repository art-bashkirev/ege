def to12(n: int) -> list:
    s = []
    while n > 0:
        s.append(n % 12)
        n //= 12
    return list(reversed(s))

n = 0

for i in range(1, 10**9):
    c = to12(i)
    if len(c) == 5:
        if c.count(7) == 1:
            cnt = 0
            for d in c:
                if d > 8:
                    cnt += 1
            if cnt > 3:
                continue
            else:
                n += 1
                print(n)
