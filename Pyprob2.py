#Problem 2: Factorial
#Write a function to calculate the factorial of a given number.

fact = int(input("enter the number:\t"))

if (fact==0 or fact==1):
    print("Factorial of ",fact, " is 1")
    quit()
else:
    ctr = 1 
    while (fact>1):
        ctr = ctr * fact
        fact-=1
print("Factorial of ",fact, " is ", ctr)
