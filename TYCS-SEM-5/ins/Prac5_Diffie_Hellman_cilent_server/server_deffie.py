import socket
import random

# Diffie-Hellman parameters
p = int(input("enter prime number : "))  # prime number
g = int(input("enter g : "))  

# Generate server private key
a = int(input(f'enter private key (less than {p-2}) :'))
A = pow(g, a, p)  # Server public key


server_socket = socket.socket()
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening...")

conn,addr = server_socket.accept()
print(f"Connected by {addr}")

# Send public parameters and server public key
conn.send(f"{p},{g},{A}".encode())

# Receive client public key
B = int(conn.recv(1024).decode())
print(f"Received client public key: {B}")

# Compute shared secret
shared_secret = pow(B, a, p)
print(f"Shared secret (server): {shared_secret}")

conn.close()
server_socket.close()
