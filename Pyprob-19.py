#Problem 19: Anagram
#Write a function that checks if two strings are anagrams of each other.

'''
Anagrams are words or phrases formed by rearranging the letters of another word or phrase to produce a new word or phrase.
In the context of strings, two strings are considered anagrams of each other if they contain the same characters with the same frequency, but in a different order.
'''

word1= input('Enter the first string: ').lower().replace(' ','')
word2= input('Enter the second string: ').lower().replace(' ','')

def isAnagram(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Length of the both strings are not equal, Not Anagram!")
    
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
    
Res = isAnagram(word1, word2)

if Res is True:
    print(word1, ' and ', word2, ' are Anagrams.')
else:
    print(word1, ' and ', word2, ' are not Anagrams.')
