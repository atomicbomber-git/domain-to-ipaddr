import socket
import sys

domain_name = sys.argv[1]
domain_info = socket.getaddrinfo(domain_name, 80)

ipv4_addresses = []
for item in domain_info:
    ipv4_addresses.append(item[4][0])

print(domain_name + " " + " ".join(ipv4_addresses))