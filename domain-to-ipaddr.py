import socket
import sys

domain_name = sys.argv[1]
ipv4_addr = socket.gethostbyname(domain_name)

print(ipv4_addr)