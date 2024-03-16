#Problem 23: Caesar Cipher with Key
#Extend the Caesar Cipher program to include a user-defined key for encryption and decryption.

all='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_encrypt(text,shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('A') - shift)%26
            encrypted_text += all[shifted]
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = (ord(char) - ord('A') + shift)%26
            decrypted_text += all[shifted]
        else:
            decrypted_text += char
    return decrypted_text

txt= input("Enter your text: ").upper()
key = int(input('Enter your key: '))
print(txt)
enc = caesar_encrypt(txt,key)
dec = caesar_decrypt(enc,key)
print(enc)
print(dec)
