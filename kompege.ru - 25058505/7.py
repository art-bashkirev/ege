from math import *

pix = 1024 * 768 # pix
N = 4096 # colors
i = ceil(log2(N))
Vimage = pix * i # bits per image
vchannel = 1_310_720 # bits per second
Tpack = 300 # seconds per package

Vpack = Tpack * vchannel # bits per package
print(Vpack / Vimage)