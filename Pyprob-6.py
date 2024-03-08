#Problem 6: String Reversal
#Write a function that reverses a given string without using the reverse method.

def rev(text):
    txt_rev =''
    for i in range(len(text)):
        txt_rev+= text [len(text)-1-i]
    return txt_rev

#-----------------------------------------------------------------------------------

#Write a function that reverses the words in a string without reversing the whole string. 
#for example: Hello this is hadi, it becomes: olleH siht si idah

def rev_words(txt):
    words = []
    res = ''
    words = txt.split()
    for word in words:
        res+= rev(word)+' '
    return res

txt = input("Enter your string:\n")
print(rev(txt))
print(rev_words(txt))
