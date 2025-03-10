a = lambda x: x - 2
b = lambda x: x // 2

from itertools import product
c = 0
for i in range(1, 25):
    for path in product([a, b], repeat=i):
        # Execution
        n = 38
        traj = [n]
        for command in path:
            n = command(n)
            traj.append(n)
        if n == 2 and 16 in traj:
            c += 1
            print(c)