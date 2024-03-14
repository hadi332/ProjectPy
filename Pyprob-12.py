#Problem 12: Collatz Conjecture
#Write a function that implements the Collatz Conjecture for a given starting number.
# a sequence that looks to reach the value 1 from any value you give it + you should calculate the number of the steps that you have take them
# you firestly get the number: 
# if even, new_num = number /2 
# if odd: new_num = (3*number) +1

def collatz_conj(num):
    result=''
    ctr =0
    while(num>1):
        if (num%2==0):
            num=int(num/2)
            result+=str(num)+','
            ctr+=1
        else:
            num=3*num+1
            result+=str(num)+','
            ctr+=1
    
    return result , ctr

number= int(input("Enter your number: "))
series, steps = collatz_conj(number)

print("the series for the given number ", number, " is ", series , " after ", steps, " steps.")
