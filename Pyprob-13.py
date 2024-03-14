#Problem 13:File Word Count
#Write a program that reads a text file and counts the occurrences of each word.

with open('text.txt') as file:
    content = file.read()
    print(content)

unique = []
words = content.split()
for w in words:
    if w not in unique:
        unique.append(w)

def occurrence(word):
    ctr = 0
    for k in words:
        if k == word:
            ctr+=1
    return ctr

dic_word = {}
for w in unique:
    val = occurrence(w)
    dic={w: val}
    dic_word.update(dic)

print(dic_word)      
file.close()
