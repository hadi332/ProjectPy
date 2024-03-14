#Problem 15: Armstrong Number
#Write a program to check if a given number is an Armstrong number.

#An Armstrong number, also known as a narcissistic number, is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

def isArmstrong(num):
    exp = len(str(num))
    res = 0
    for i in str(num):
        res += int(i)**exp
    if res == num:
        return True
    else:
        return False
    
number = int(input("Enter a number: "))
val = isArmstrong(number)

if val is True:
    print(number, " is an Armstrong number.")
else: 
    print(number, " is not an Armstrong number.")
