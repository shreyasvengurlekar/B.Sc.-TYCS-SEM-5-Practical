text = input ("Enter Your text : ");
key =  input ("Enter Your key : ");

# text = "shreyas"
# key = "key"

def encrypt(text, key):
    encrypted = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)].lower()) - 97
            base = ord('a')
            encrypted += chr((ord(char.lower()) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(text, key):
    decrypted = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift = ord(key[i % len(key)].lower()) - 97
            base = ord('a')
            decrypted += chr((ord(char.lower()) - base - shift + 26) % 26 + base)
        else:
            decrypted += char
    return decrypted

# Example usage:
cipher = encrypt(text, key)
print("Encrypted:", cipher)


original = decrypt(cipher, key)
print("Decrypted:", original)
