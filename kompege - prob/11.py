l = 248
ns = 75600
vs = 16 * 1024 * 1024 # bytes

import math
sz = vs / ns # bytes per number

szb = sz * 8 # bits per number

i = szb / 248 # bits

assert (248 * i) / 8 == sz
print(i)
i = math.ceil(i)
print(i)


assert ns * l * i / 8 >= vs

print(ns * l * i / 8, vs)
print(2 ** i)
