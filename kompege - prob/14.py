def b(n):
    s = []
    while n > 0:
        s.append(n % 7)
        n //= 7
    return s[::-1]

m = 73

for x in range(1, 2030+1):
    expr = 7 **170 + 7 **100 - x
    s = b(expr)
    if s.count(0) == 73:
        print(x)
    
print(m)