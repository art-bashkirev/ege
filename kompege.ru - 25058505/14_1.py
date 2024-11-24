from string import digits, ascii_uppercase

a = (digits + ascii_uppercase)[:19]

for x in reversed(a):
    l = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if int(x, 19) % 18 == 0:
        print(l % 18)
