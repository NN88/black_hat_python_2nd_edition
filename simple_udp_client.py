import socket

# vars
target_host = '127.0.0.1'
target_port = 9997

# create a socket object
# AF_INET = ip4
# SOCK_DGRAM = udp
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# no need to connect like TCP
# Because UDP is a connectionless protocol, there is 
# no call to connect() beforehand

# send some data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# receive some data
# You will also notice that it returns both the data and the
# details of the remote host and port. 
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()




