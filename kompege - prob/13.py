from ipaddress import ip_network, ip_address

net = ip_network("172.16.192.0/255.255.192.0")
c = []

for i in net:
    if bin(int(i))[2:].count("1") % 5 != 5 and bin(int(i))[2:][-14:] != "0" * 14 and bin(int(i))[2:][-14:] != "1" * 14:
        #print(bin(int(i))[2:][-14:], bin(int(i))[2:])
        c.append(i)
    
    
print(len(c))