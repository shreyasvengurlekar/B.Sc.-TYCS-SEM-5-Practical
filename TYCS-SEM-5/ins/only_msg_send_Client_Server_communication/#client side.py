#client side 
import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

while True:
    message = input("Enter message send to server --> ")
    if message.lower() == 'exit':
        print("Exiting client.")
        break
    client.sendall(message.encode('utf-8'))
    response = client.recv(4096)
    print("Received from server --> ", response.decode('utf-8'))

client.close()
