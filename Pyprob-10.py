#Problem 10: Caesar Cipher
#Implement a basic Caesar Cipher encryption and decryption program.

all='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

txt= input("Enter your text: ").upper()

def caesar_encrypt(text):
    encrypted_text = ""
    base = ord('A')
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - base - 3)%26
            encrypted_text += all[shifted]
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text):
    decrypted_text = ""
    base = ord('A')
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - base + 3)%26
            decrypted_text += all[shifted]
        else:
            decrypted_text += char
    return decrypted_text

print(txt)
enc = caesar_encrypt(txt)
dec = caesar_decrypt(enc)
print(enc)
print(dec)
