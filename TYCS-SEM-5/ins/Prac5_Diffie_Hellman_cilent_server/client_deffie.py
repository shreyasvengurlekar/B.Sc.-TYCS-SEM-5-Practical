import socket
import random

# Connect to server
client_socket = socket.socket()
client_socket.connect(('localhost', 12345))

# Receive p, g, A from server
data = client_socket.recv(1024).decode()
p, g, A = map(int, data.split(','))
print(f"Received from server: p={p}, g={g}, A={A}")

# Generate client private key
b = int(input(f'enter private key(less than {p-2}) : '))
B = pow(g, b, p)  # Client public key

# Send client public key to server
client_socket.send(str(B).encode())

# Compute shared secret
shared_secret = pow(A, b, p)
print(f"Shared secret (client): {shared_secret}")

client_socket.close()
