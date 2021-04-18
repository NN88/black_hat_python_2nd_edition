# Simple TCP Client (POC)
import socket

target_host = "172.16.103.139"
target_port = 80

# create a socket object
# AF_INET indicates ip4
# SOCK_STREAM indicates that this will be a TCP Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHOST:172.16.103.139\r\n\r\n")

#receive some data
response = client.recv(4096)

print(response.decode())
client.close()

# Assumptions:
# connection will always succeed.
# server expects us to send data first.
# server will return data in a timely manner.

# Notes
# While programmer have varied opinions about how to deal with
# blocking sockets, exception-handling in sockets, and the like,
# it's quite rare for pentesters to build these niceties into
# their quick-and-dirty tool for recon or exploitation work,
# so we'll omit them.