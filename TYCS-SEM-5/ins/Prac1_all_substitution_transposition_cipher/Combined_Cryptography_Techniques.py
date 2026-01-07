# Combined Code

def ceaser_cipher_encrypt(plain_text, key):
    result = ''
    for i in plain_text:
        if i.isupper():
            result += chr((ord(i) + key - 65) % 26 + 65)
        else:
            result += chr((ord(i) + key - 97) % 26 + 97)
    return result

def ceaser_cipher_decrypt(encrpyt_text, key):
    result = ''
    for i in encrpyt_text:
        if i.isupper():
            result += chr((ord(i) - key - 65) % 26 + 65)
        else:
            result += chr((ord(i) - key - 97) % 26 + 97)
    return result

def mono_encrypt(text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    key = "qwertyuiopasdfghjklzxcvbnm"
    encrypted = ""
    for char in text.lower():
        if char in plain:
            index = plain.index(char)
            encrypted += key[index]
        else:
            encrypted += char
    return encrypted

def mono_decrypt(cipher):
    plain = "abcdefghijklmnopqrstuvwxyz"
    key = "qwertyuiopasdfghjklzxcvbnm"
    decrypted = ""
    for char in cipher.lower():
        if char in key:
            index = key.index(char)
            decrypted += plain[index]
        else:
            decrypted += char
    return decrypted

def multiplicative_encrypt(plain_text, key):
    result = ''
    for char in plain_text.lower():
        if char.isalpha():
            result += chr(((ord(char) - 97) * key) % 26 + 97)
        else:
            result += char
    return result

def multiplicative_decrypt(cipher_text, key):
    def mod_inverse(k):
        for i in range(1, 26):
            if (k * i) % 26 == 1:
                return i
        return None

    inverse = mod_inverse(key)
    if inverse is None:
        return "Invalid key! No modular inverse exists."
    
    result = ''
    for char in cipher_text.lower():
        if char.isalpha():
            result += chr(((ord(char) - 97) * inverse) % 26 + 97)
        else:
            result += char
    return result

def poly_encrypt(plain_text, key):
    encrypted = ''
    key = key.lower()
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                encrypted += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted += chr((ord(char) + shift - 97) % 26 + 97)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def poly_decrypt(cipher_text, key):
    decrypted = ''
    key = key.lower()
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                decrypted += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted += chr((ord(char) - shift - 97) % 26 + 97)
            key_index += 1
        else:
            decrypted += char
    return decrypted

def rail_fence_encrypt(text, rails):
    fence = ['' for _ in range(rails)]
    rail = 0
    var = 1
    for char in text:
        fence[rail] += char
        rail += var
        if rail == 0 or rail == rails - 1:
            var = -var
    return ''.join(fence)

def rail_fence_decrypt(cipher, rails):
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    pos = [pattern[i % len(pattern)] for i in range(len(cipher))]
    rail_counts = [pos.count(r) for r in range(rails)]
    
    rail_strings = []
    i = 0
    for count in rail_counts:
        rail_strings.append(cipher[i:i+count])
        i += count

    rail_indices = [0] * rails
    result = ''
    for r in pos:
        result += rail_strings[r][rail_indices[r]]
        rail_indices[r] += 1
    return result

def vernam_cipher(text, key):
    cipher = ''
    for i in range(len(text)):
        cipher += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return cipher

# MAIN MENU
while True:
    print("\nChoose Technique Type:")
    print("1. Substitution Technique")
    print("2. Transposition Technique")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nSubstitution Methods:")
        print("1. Caesar Cipher")
        print("2. Monoalphabetic Cipher")
        print("3. Multiplicative Cipher")
        print("4. Polyalphabetic Cipher (Vigenère)")
        sub_choice = input("Enter your choice: ")

        message = input("Enter the message: ")

        if sub_choice == '1':
            key = int(input("Enter the key: "))
            enc = ceaser_cipher_encrypt(message, key)
            print("Encrypted:", enc)
            print("Decrypted:", ceaser_cipher_decrypt(enc, key))

        elif sub_choice == '2':
            enc = mono_encrypt(message)
            print("Encrypted:", enc)
            print("Decrypted:", mono_decrypt(enc))

        elif sub_choice == '3':
            key = int(input("Enter the multiplicative key (coprime with 26): "))
            enc = multiplicative_encrypt(message, key)
            print("Encrypted:", enc)
            print("Decrypted:", multiplicative_decrypt(enc, key))

        elif sub_choice == '4':
            key = input("Enter the key string: ")
            enc = poly_encrypt(message, key)
            print("Encrypted:", enc)
            print("Decrypted:", poly_decrypt(enc, key))

    elif choice == '2':
        print("\nTransposition Methods:")
        print("1. Rail Fence Cipher")
        print("2. Vernam Cipher")
        trans_choice = input("Enter your choice: ")

        message = input("Enter the message: ")

        if trans_choice == '1':
            rails = int(input("Enter number of rails: "))
            enc = rail_fence_encrypt(message, rails)
            print("Encrypted:", enc)
            print("Decrypted:", rail_fence_decrypt(enc, rails))

        elif trans_choice == '2':
            key = input("Enter the key (same length or shorter): ")
            enc = vernam_cipher(message, key)
            print("Encrypted (raw XOR):", enc)
            print("Decrypted (raw XOR):", vernam_cipher(enc, key))

    elif choice == '0':
        break

    else:
        print("Invalid choice. Try again.")
