from fractions import Fraction
from math import log2, ceil

N = 1025
i = ceil(log2(N))

per_number = ((693 * 1024 * 8) / 2000) # bytes

l = per_number // i

print(l)

print(int("1000", 2))