import hashlib
import time

def sha1_hash():
    msg1 = input("Enter first message : ")
    msg2 = input("Enter second message : ")

    print("\nEncoding the input string into bytes and hashing them using Sha1...")

    data1 = hashlib.sha1(msg1.encode())
    data2 = hashlib.sha1(msg2.encode())

    print("\nSha1 hash of the first message in hexadecimal format:\n")
    print(data1.hexdigest())
    print("\nSha1 hash of the second message in hexadecimal format:\n")
    print(data2.hexdigest())


def md5_hash():
    msg1 = input("Enter first message : ")
    msg2 = input("Enter second message : ")

    print("\nEncoding the input string into bytes and hashing them using MD5...")

    data1 = hashlib.md5(msg1.encode())
    data2 = hashlib.md5(msg2.encode())

    print("\nMD5 hash of the first message:\n", data1.digest())
    print("\nMD5 hash of the second message:\n", data2.digest())


def file_handling():
    # File reading
    filepath = input("Enter file path: ")
    try:
        with open(filepath, 'r') as file:
            txt = file.read()
        print("\nFile Content:\n", txt)
    except FileNotFoundError:
        print("\nError: File not found.")
        return

    # Sub-menu for file hashing
    while True:
        print("\nChoose hashing method for file content:")
        print("1. SHA1")
        print("2. MD5")
        choice = input("Enter choice (1 or 2): ")
        
        if choice == "1":
            a = hashlib.sha1(txt.encode())
            print("\nSHA1 hash of data inside file:\n", a.hexdigest())
            break
        elif choice == "2":
            b = hashlib.md5(txt.encode())
            print("\nMD5 hash of data inside file:\n", b.digest())
            break
        else:
            print("Invalid choice. Please enter 1 or 2 only.")

# Main menu
while True:
    print("\nMain Menu:")
    print("1. SHA1 Hashing ")
    print("2. MD5 Hashing")
    print("3. File Handling with Hashing")
    print("4. Exit")
    
    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        sha1_hash()
        time.sleep(2)
    elif main_choice == "2":
        md5_hash()
        time.sleep(2)
    elif main_choice == "3":
        file_handling()
        time.sleep(2)
    elif main_choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")
        time.sleep(2)