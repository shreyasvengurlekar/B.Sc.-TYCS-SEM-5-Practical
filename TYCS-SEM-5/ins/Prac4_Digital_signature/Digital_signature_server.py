# python --version
# python -m ensurepip --upgrade
# python -m pip install --upgrade pip
# python -m pip install pycryptodome


from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto import Random

# Sender: Enter your message
message = input("Sender: Enter your message: ")

# Save the message into message.txt
with open("message.txt", "w") as f:
    f.write(message)

# Generate RSA key pair (2048-bit)
random_generator = Random.new().read
key_pair = RSA.generate(2048, random_generator)

# Export public and private keys
public_key = key_pair.publickey().export_key()
private_key = key_pair.export_key()

print("\nSender Public Key:\n")
print(public_key.decode())

# Function to generate digital signature
def generate_signature(private_key, message):
    key = RSA.import_key(private_key)
    hashed_message = SHA256.new(message.encode("utf-8"))
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hashed_message)
    return signature

# Generate the digital signature
signature = generate_signature(private_key, message)

# Save public key
with open("public_key.txt", "wb") as f:
    f.write(public_key)

# Save private key
with open("private_key.txt", "wb") as f:
    f.write(private_key)

# Save signature
with open("signature.sig", "wb") as f:
    f.write(signature)

# Final status messages
print("\nSender: All data saved successfully.")
print(f"Sender: Message sent successfully → {message}")
print("Sender: Digital signature generated and saved using PKCS1_v1_5.")
