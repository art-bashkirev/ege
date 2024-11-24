from math import sqrt

def m(x: int):
    divisors = set()
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            divisors.add(i)
            if i != x // i:
                divisors.add(x // i)
    if len(divisors) == 0:
        return None
    return min(divisors) + max(divisors)

n = 800_001
c = 0

while c < 5:
    mval = m(n)
    if mval:
        if str(mval)[-1] == "4":
            print(n, mval)
            c += 1
    else:
        continue
    n += 1