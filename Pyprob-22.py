#Problem 22: Common Elements
#Write a function that returns the common elements between two lists.

def commons(list1, list2): 
    common =[]
    for l in range(len(list1)):
        for j in range(len(list2)):
            if list1[l]==list2[j]:
                common.append(list2[j])
                     
    return  common

list_one = [1,3,4,88,5,6,77,8,9]
list_two = [11,88,44,5,8,9,65547]

result = commons(list_one,list_two)

print('The commons are ', result)
