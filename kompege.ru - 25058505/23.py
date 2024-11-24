
from itertools import *

def a(x):
    return x - 2

def b(x):
    return x // 2

paths = 0

for i in range(60):
    for path in product([a, b], repeat=i):
        n = 38
        traj = []
        for function in path:
            traj.append(function(n))
            n = function(n)
        if n == 2 and 16 in traj:
            paths += 1
            print(paths)