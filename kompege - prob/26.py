from operator import itemgetter, attrgetter

with open("26.txt") as f:
    n, k = map(int, f.readline().split())
    data = []
    for _ in range(n):
        p = list(map(int, f.readline().split()))
        ps = [-p[0], p[1] + p[2] + p[3] + p[4], p[4]]
        data.append(ps)

s = (sorted(data, key=itemgetter(1, 2, 0), reverse=True))
for i in range(k):
    print(s[i])

for i in range(k-1, k+10):
    print(*s[i])