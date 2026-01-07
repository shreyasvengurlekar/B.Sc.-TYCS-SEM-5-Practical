import socket

# Function to check prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# GCD function
def gcd(a, h):
    while h != 0:
        temp = h
        h = a % h
        a = temp
    return a

# Multiplicative inverse
def multiplicative_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

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

    # Data format: p,q,pt
    try:
        p, q, pt = map(int, data.decode().split(','))
    except:
        client_socket.sendall("Invalid input format.".encode())
        continue

    # Check primes
    if not (is_prime(p) and is_prime(q)):
        client_socket.sendall("Error: Both numbers must be prime.".encode())
        continue

    # RSA base calculation
    n = p * q
    phi = (p - 1) * (q - 1)

    # Check if plaintext is smaller than n
    if pt >= n:
        client_socket.sendall(f"Error: Plain text must be less than n ({n}).".encode())
        continue

    # Choose e
    e = 3
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 2

    d = multiplicative_inverse(e, phi)

    # Encrypt
    c = pow(pt, e, n)

    # Decrypt
    m = pow(c, d, n)

    result = f"Public key: {e}\nPrivate key: {d}\nEncrypted: {c}\nDecrypted: {m}"
    client_socket.sendall(result.encode())

client_socket.close()
server.close()
print("Connection closed.")
