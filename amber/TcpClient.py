import socket

target_host = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
msg = "aaaa"
client.send(bytes(msg,'utf-8'))

response = client.recv(4096)

print(response)
