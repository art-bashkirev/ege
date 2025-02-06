# No. 216 kompege.ru

f = lambda x, a: ((x & 26 != 0) or (x & 13 != 0) ) <= ((x & 29 == 0) <= (x & a  != 0) )

def v(a):
  return all( f(x, a) for x in range(1, 1000) )

for a in range(1, 1000):
  if v(a):
    print(a) 
    break