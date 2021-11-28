import socket
import threading
server_ip = "0.0.0.0"
server_port = 9999
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((server_ip,server_port))
server.listen(5)
print("[*]Listening on %s:%d"%(server_ip,server_port))
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Recevied: %s"%request)
    client_socket.send(bytes("ACK!","utf-8"))
    client_socket.close()
while True:
    client,address = server.accept()
    print("[*] Accepted connection from:%s:%d"%(address[0],address[1]))
    client_handler = threading.Thread(target=handle_client,args=(client,),name="threading")
    client_handler.start()


