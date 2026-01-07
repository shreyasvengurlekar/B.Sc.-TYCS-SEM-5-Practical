import hmac
import hashlib

def generate_mac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

def verify_mac(key, message, mac_to_verify):
    generated_mac = generate_mac(key, message)
    return hmac.compare_digest(generated_mac, mac_to_verify)

key = input("Enter secret key: ")
msg = input("Enter the message: ")

# Generate MAC
mac = generate_mac(key, msg)
print("\n Generated MAC (HMAC-SHA256): ", mac)

# verification
recv_mac = input("\n Enter MAC to verify: ")

# Verification
if verify_mac(key, msg, recv_mac):
    print("MAC is valid. Data is authentic and inaltered.")
else:
    print("MAC is invalid. Data may have been tampered.")
