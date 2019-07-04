import socket
import sys

domain_name = sys.argv[1]
domain_info = socket.getaddrinfo(domain_name, 80)

ipv4_addresses = []
for item in domain_info:
    address = item[4][0]
    if address not in ipv4_addresses:
        ipv4_addresses.append(address)

print(domain_name + " " + " ".join(ipv4_addresses))