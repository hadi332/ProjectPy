#Problem 31: Title Case
#Write a function that converts a given sentence to title case (capitalize the first letter of each word).

def title_cap(string):
    final = ''
    lista = string.split()
    
    for word in lista:
        final += word[0].upper() + word[1:] + ' '
    return final

text = input('Enter your title: ')
print(title_cap(text))
