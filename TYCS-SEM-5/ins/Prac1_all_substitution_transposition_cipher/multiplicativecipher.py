def multiplicative_cipher(text,key):
    encrypted=""
    decrypted=""

    #Encrypt
    for char in text:
        if char.isalpha():
            num=ord(char.upper())-65
            enc=(num*key)%26
            encrypted+=chr(enc + 65)
        else:
            encrypted+=char

    #Decrypt
    try:
        inv_key=pow(key,-1,26)
    except ValueError:
        return "Invalid key: No modular inverse exist"

    for char in encrypted:
        if char.isalpha():
            num=ord(char.upper())-65
            dec=(num*inv_key)%26
            decrypted+=chr(dec + 65)
        else:
            decrypted+=char

    print("Encrypted:",encrypted)
    print("Decrypted:",decrypted)
multiplicative_cipher("Shreyas",3)
