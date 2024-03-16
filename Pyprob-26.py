#Problem 26: Largest Element in a List
#Write a function that finds the largest element in a list.

def max_val(lista):
    val = 0
    for num in lista:
        if num >= val:
            val = num
    return val

list_nu = [1,2,8,4,6,9,10,2,4]

max_value = max_val(list_nu)
print(max_value)
