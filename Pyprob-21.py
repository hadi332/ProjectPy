#Problem 21: Reverse a List
#Write a function to reverse the elements of a list.

def reverse_list(lista):
    rev =[]
    for l in range(len(lista)):
        rev.append(lista[len(lista)-1-l])
    return rev

list_1= [1,2,4,3,8,7,6]
rev_list = reverse_list(list_1)
print("reversed list is ", rev_list)
