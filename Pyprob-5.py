#Problem 5: Guess the Number
#Create a simple "Guess the Number" game where the computer generates a random number, and the user has to guess it.
#You should show after how many trials you guessed the number. 

from random import randint

a = randint(0,100)
ctr = 1
guess = int(input("Enter your guess: "))

while (True):
    if (a>guess):
        print("Too Low!")
        guess = int(input("Enter your new guess: "))
        ctr +=1
    elif (a<guess):
        print("Too High!")
        guess = int(input("Enter your new guess: "))
        ctr +=1
    elif (a == guess): 
        print("Your guess is True")
        break

print("You have guessed ", a, " after ", ctr, " times!")
