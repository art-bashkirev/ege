from itertools import permutations, product

f = lambda x, y, w, z: ((w <= y) <= x) or (not z)

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, a2, 1, a3), (a4, 0, a5, a6), (a7, 1, 0, 0)]
    ans = [0,0,0]

    if len(set(table)) != len(table):
        continue

    for p in permutations('xywz'):
        if list(f(**dict(zip(p, row))) for row in table) == ans:
            print(" ".join(map(str, p)))