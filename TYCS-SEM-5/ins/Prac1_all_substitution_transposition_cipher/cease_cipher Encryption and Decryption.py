plain_text =input("Enter plain_text:-")
key= int(input('Enter the key value : '))

def ceaser_cipher_encrypt(plain_text,key):
    result=''
    for i in plain_text:
        if i.isupper():
            result+=chr((ord(i)+key-65)%26+65)
        else:
            result+=chr((ord(i)+key-97)%26+97)
    return result
encrpyt_text= ceaser_cipher_encrypt(plain_text, key)
print("Encrypt text : ",encrpyt_text)

def ceaser_cipher_decrypt(encrpyt_text,key):
    result=''
    for i in encrpyt_text:
        if i.isupper():
            result+=chr((ord(i)-key-65)%26+65)
        else:
            result+=chr((ord(i)-key-97)%26+97)
    return result
            
print("Decrypted text : ",ceaser_cipher_decrypt(encrpyt_text, key))
