#file handling
import hashlib

#create a file named input.txt and write some text in it before running this code

#reading content from a file
with open('input.txt', 'r') as file:
    txt= file.read()
print("File Content:\n", txt);

#sha1 hashing
a = hashlib.sha1(txt.encode());
print("\nSHA1 hash of data inside file:\n", a.hexdigest());

#md5 hashing
b = hashlib.md5(txt.encode());
print("\nMD5 hash of data inside file:\n", b.digest());