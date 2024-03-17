#Problem 29: String Compression
#Write a function that performs basic string compression. For example, the string "aabcccccaaa" would become "a2b1c5a3".

def count_char(string):
    ctr = 1
    res =''

    for i in range(1, len(string)-1):
        if string[i]==string[i-1]:
            ctr +=1
        else: 
            res+= string[i-1] + str(ctr)
            ctr =1

    res += string[-1]+str(ctr)
    return res

array = input("Enter your string: ")
ch= count_char(array)

print(f"your new array is {ch}")
