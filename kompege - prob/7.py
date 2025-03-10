pix = 1280 * 960
palette = 2048
bits = 11
assert palette == 2 ** bits

imgsz = bits * pix # bits
packet_sz = 132 * 96_468_992 # bits

n = packet_sz // imgsz
assert imgsz * n < packet_sz

print(n)