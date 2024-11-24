from ipaddress import ip_address, ip_network

net = ip_network("172.16.168.0/255.255.248.0")
c = 0
for ip in net:
    if bin(int(ip))[2:].count("1") % 5 != 0:
        c += 1

print(c)