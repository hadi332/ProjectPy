#Problem 4: Fibonacci Series
#Write a program to generate the Fibonacci series up to a specified number of terms.

n = int(input("Enter your number: "))
fib_series = [0,1]

for _ in range(2,n+1):
    next_term = fib_series[-1] + fib_series[-2]
    fib_series.append(next_term)

print("Fibonacci Series to order ", n, " is " , fib_series)
