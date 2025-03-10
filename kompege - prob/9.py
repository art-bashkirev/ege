from collections import Counter

with open("9.csv") as f:
    data = [list(map(int, r)) for r in list(x.split(";") for x in f.readlines())]
co = 0
for row in data:
    c = Counter(row)
    rep = sum(i for i in c if c[i] == 3)
    non_rep = sum(i for i in c if c[i] == 1)
    if list(c.values()).count(3) == 1 and list(c.values()).count(1) == 3:
        if  (3 * rep) ** 2 > non_rep ** 2:
            co += 1
            
print(co)