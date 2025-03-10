def R(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = "10" + s
    else:
        s = "1" + s + "01"
    return int(s, 2)

for i in range(1, 13):
    print(R(i))