#Problem 8: Rock, Paper, Scissors
#Implement a simple text-based Rock, Paper, Scissors game where the user can play against the computer.

import random

guess = ['Rock', 'Paper', 'Scissors']
pc_guess = random.choice(guess)

H_guess = input("Enter your choice: ")
while (H_guess != 'q'):

    print('Computer chose ', pc_guess)
  
    if (H_guess == "Rock" and pc_guess == 'Paper'):
        print('You Lost! Computer Won!')
    elif (pc_guess == "Rock" and H_guess == 'Paper'):
        print('You Won! Computer Lost!')

    elif (H_guess == "Rock" and pc_guess == 'Scissors'):
        print('You Lost! Computer Won!')
    elif (pc_guess == "Rock" and H_guess == 'Scissors'):
        print('You Won! Computer Lost!')

    elif (H_guess == "Paper" and pc_guess == 'Scissors'):
        print('You Lost! Computer Won!')
    elif (pc_guess == "Paper" and H_guess == 'Scissors'):
        print('You Won! Computer Lost!')
    
    H_guess = input("Enter your choice: ")
