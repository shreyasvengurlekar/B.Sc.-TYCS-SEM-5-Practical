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

message = input("Enter string: ")
cipher = mono_encrypt(message)
print("Encrypted:", cipher)

original = mono_decrypt(cipher)
print("Decrypted:", original)
