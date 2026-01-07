
import hashlib

#Taking two input from the user
msg1= input("Enter first message : ");
msg2= input("Enter second message : ");

# Encoding the input string into bytes and hashing them using Sha1
print("\nEncoding the input string into bytes and hashing them using Sha1...")
data1= hashlib.sha1(msg1.encode());
data2= hashlib.sha1(msg2.encode());

# Returns the Sha1 hash in hexadecimal format
print("\nSha1 hash of the first message in hexadecimal format:\n", data1.hexdigest());
print("\nSha1 hash of the second message in hexadecimal format:\n", data2.hexdigest());