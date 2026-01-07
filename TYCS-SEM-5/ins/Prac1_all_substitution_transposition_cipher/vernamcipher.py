import random
import base64

def generate_key(length):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))

def encrypt(text, key):
    result = ''
    for t, k in zip(text, key):
        result += chr(ord(t) ^ ord(k))
    return base64.b64encode(result.encode()).decode()

def decrypt(encoded_text, key):
    decoded = base64.b64decode(encoded_text).decode()
    result = ''
    for c, k in zip(decoded, key):
        result += chr(ord(c) ^ ord(k))
    return result

# Main program
plain_text = input("Enter the text to encrypt: ")
key = generate_key(len(plain_text))

cipher_text = encrypt(plain_text, key)
decrypted_text = decrypt(cipher_text, key)
print("-----Result------")
print(f"Plain Text: {plain_text}")
print(f"Key       : {key}")
print(f"Encrypted : {cipher_text}")
print(f"Decrypted : {decrypted_text}")
