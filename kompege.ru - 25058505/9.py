from collections import Counter

d = [list(map(int, i.split())) for i in open("9_17863.csv")]

t = []
for row in d:
    c = Counter(row)
    p = []
    sw = "FUCK"
    for i in c:
        if c[i] == 3:
            sw = i
    for i in c:
        if i == sw:
            continue
        if c[i] > 1:
            sw = "FUCK"
        else:
            p.append(i)
    if sw == "FUCK":
        continue
    if (sw * 3) ** 2 > (sum(p)) ** 2:
        t.append(row)

print(len(t))