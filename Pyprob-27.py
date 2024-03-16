#Problem 27: Sum of Primes
#Write a program to find the sum of all prime numbers within a given range.

def isPrime(num):
    if (num<2):
        return False
    
    for n in range(2, int(num**0.5)+1):
        if num%n==0:
            return False
    else:
        return True
        
def list_of_primes(number):
    primes=[]
    for i in range(number+1):
        if isPrime(i):
            primes.append(i)
    return primes

def sum_of_primes(lista):
    sum=0
    for i in range(len(lista)):
        sum += lista[i]
    return sum

nb = int(input("Enter your range: "))

prime_numbers = list_of_primes(nb)
print(prime_numbers)
print(sum_of_primes(prime_numbers))
