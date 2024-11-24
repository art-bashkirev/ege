def r(n):
    s = f"{n:b}"
    if n % 2 == 0:
        s += "10"
    else:
        s = "1" + s
        s += "01"

    return int(s, 2)

for i in range(1, 13):
    print(r(i))
