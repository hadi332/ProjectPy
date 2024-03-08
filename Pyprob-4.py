#Problem 4: Fibonacci Series 
#Write a program to generate the Fibonacci series up to a specified number of terms, using recursive method

n = int(input("Enter your number: "))

def fab(num):
    if num==0:
        return 0
    elif (num==1 or num==2):
        return 1
    else:
        return fab(num-1)+fab(num-2)

result = fab(n)

print("result is ", result)
#----------------------------------------------------------------------------------------------
#Write a program to generate the Fibonacci series up to a specified number of terms, using iterative method
n = int(input("Enter your number: "))

