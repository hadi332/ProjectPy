#Guess the Number: The computer selects a random number between a specified range, and the player tries to guess it.
#The computer provides hints such as "too high" or "too low" after each guess until the player guesses the correct number.

from random import randint

computer_number = randint(1,100)

def guess(num):
    ctr = 0
    while True:
        if num > computer_number:
            print('Too High!')
            num = int(input("Enter a number: "))
            ctr +=1
        elif num < computer_number:
            print('Too Low!')
            num = int(input("Enter a number: "))
            ctr +=1
        else:
            ctr +=1
            print(f'Congratulations! You have guessed the number {computer_number} after {ctr} times!')
            break
   
nb_user = int(input("Enter a number: "))
guess(nb_user)
