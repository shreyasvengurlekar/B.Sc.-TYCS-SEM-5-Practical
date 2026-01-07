import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Server is listening on port 9999...")

client_socket, addr = server.accept()
print(f"Connected to {addr}")

while True:
    data = client_socket.recv(4096)
    if not data:
        break
    print("Received from client --> ", data.decode('utf-8'))
    msg = input("Enter message to send to client --> ")
    client_socket.sendall(msg.encode('utf-8'))
    if msg.lower() == 'exit':
        break

client_socket.close()
server.close()
print("Connection closed.")
