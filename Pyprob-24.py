#Problem 24: Vowel Counter
#Write a function that counts the number of vowels in a given string.

vowels = 'AEIOUaeiou'

def vowels_counter(txt):
    ctr = 0
    for char in range(len(txt)):
        if txt[char] in vowels:
            ctr +=1
    return ctr

text = input('Enter your text: ')
vowel = vowels_counter(text)
print('THe number of vowels in your text is: ', vowel)
