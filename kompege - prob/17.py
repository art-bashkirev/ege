with open("17.txt") as f:
    data = list(map(int, f.read().split()))
    
s = 0
for i in data:
    if abs(i) % 32 == 0:
        s += 1
print(s)
d = []

check_neg = lambda p: p[0] < 0 or p[1] < 0
check_sum = lambda p: sum(p) < s
for i in range(1, len(data)):
    pair = data[i-1], data[i]
    if check_neg(pair) and check_sum(pair):
        d.append(sum(pair))
    
print(len(d), max(d))