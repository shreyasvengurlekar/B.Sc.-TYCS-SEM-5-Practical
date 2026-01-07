import hashlib

#Taking two input from the user
msg1= input("Enter first message : ");
msg2= input("Enter second message : ");

# Encoding the input string into bytes and hashing them using MD5
print("\nEncoding the input string into bytes and hashing them using MD5...")
data1= hashlib.md5(msg1.encode());
data2= hashlib.md5(msg2.encode());

# Returns the MD5 hash in bytes
print("\nMD5 hash of the first message:\n", data1.digest());
print("\nMD5 hash of the second message:\n", data2.digest());
