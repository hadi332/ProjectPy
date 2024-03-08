#Problem 7: Prime Numbers
#Write a program to print all prime numbers in a given range.

def is_prime(num):
    if (num <2):
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
                return False
    return True

def gen_prime_list(num):
    prime_list = [i for i in range(num+1) if is_prime(i)]
    return prime_list

number=int (input('Enter your limit: '))
print("List of prime numbers to ", number, " is ", gen_prime_list(number) )
