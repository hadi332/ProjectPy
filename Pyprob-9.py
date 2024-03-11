#Problem 9: List Manipulation
#Write a program that removes duplicates from a list and sorts it in ascending order.

list_e =[]

words= input("Enter your list: ")

for word in words:
    if word not in list_e:
        list_e.append(word)
list_e.sort()
print(list_e)
