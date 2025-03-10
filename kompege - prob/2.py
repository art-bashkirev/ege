from itertools import permutations, product

f = lambda x,y,w,z: ((w <= (not (z <= x))) or y)\

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [
        (1, a1, a2, a3),
        (0, 1, 0, a4),
        (a5, 0, a6, a7)
    ]
    res = [0, 0, 0]
    if len(set(table)) == len(table):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, row))) for row in table] == res:
                print(*p)