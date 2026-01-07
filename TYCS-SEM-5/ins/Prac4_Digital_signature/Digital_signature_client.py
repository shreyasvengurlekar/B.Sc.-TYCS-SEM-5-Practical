# python --version
# python -m ensurepip --upgrade
# python -m pip install --upgrade pip
# python -m pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

# Function to verify signature
def verify_signature(public_key, message, signature):
    key = RSA.import_key(public_key)
    hashed_message = SHA256.new(message.encode("utf-8"))
    verifier = PKCS1_v1_5.new(key)
    return verifier.verify(hashed_message, signature)

# Load public key
with open("public_key.txt", "rb") as f:
    public_key = f.read()
print("Receiver: Public key loaded →\n", public_key.decode())

# Load message
with open("message.txt", "r") as f:
    message = f.read()
print("Receiver: Message received →", message)

# Load signature
with open("signature.sig", "rb") as f:
    signature = f.read()
print("Receiver: Signature loaded.")

# Verify digital signature
print("\nVerifying digital signature...")
is_valid = verify_signature(public_key, message, signature)

if is_valid:
    print("Receiver: Signature verification result → VALID")
    print("Receiver: Message authenticity confirmed.")
else:
    print("Receiver: Signature verification result → INVALID")
    print("Receiver: Message authenticity cannot be confirmed.")
