from fnmatch import fnmatch as m


for i in range(1917, 10**10, 1917):
    if m(str(i), "3?12?14*5"):
        print(i, i // 1917)