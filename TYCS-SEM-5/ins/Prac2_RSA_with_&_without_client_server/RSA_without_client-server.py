import math

# GCD function
def gcd(a, h):
    while h != 0:
        temp = h
        h = a % h
        a = temp
    return a

# important to prime numbers
p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

n = p * q
phi = (p - 1) * (q - 1)

# choose e such that e and phi(n) are co-prime
e = 3
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 2

# multiplicative inverse
def multiplicative_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

d = multiplicative_inverse(e, phi)

# message to encrypt
pt = int(input("Enter plain text (number): "))
print("Message data =", pt)

# encrypt
c = pow(pt, e, n)
print("Encrypted data =", c)

# decryption
m = pow(c, d, n)
print("Decrypted data =", m)
