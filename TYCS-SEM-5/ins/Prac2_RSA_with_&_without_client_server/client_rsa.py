import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

while True:
    try:
        p = int(input("Enter first prime number: "))
        q = int(input("Enter second prime number: "))
        pt = int(input("Enter plain text (number): "))
    except ValueError:
        print("Invalid input, please enter numbers only.")
        continue

    message = f"{p},{q},{pt}"
    client.sendall(message.encode())

    response = client.recv(4096)
    print("\n--- Server Response ---")
    print(response.decode())
    print("-----------------------\n")

    again = input("Do you want to try again? (y/n): ").strip().lower()
    if again != 'y':
        break

client.close()
print("Client closed.")
