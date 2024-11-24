a = [int(i) for i in open("17_17873.txt")]

m = min(a)
r = []

for i in range(len(a) - 1):
    p = a[i], a[i+1]
    if p[0] % 16 == m or p[1] % 16 == m:
        r.append(sum(p))

print(len(r), max(r))