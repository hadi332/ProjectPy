#Hangman: The computer selects a random word, and the player has to guess it by suggesting letters within a limited number of attempts.
#For each incorrect guess, a part of a stick figure (representing a hangman) is drawn.
#The player wins if they guess the word before the hangman is fully drawn.

# we won't draw hangman, we will use another term for lives (you have 5 lives only to win or you will lose)
from random import randint

#The below function is to create a word by computer with no repitative letters. 
def randchar(nb):
    all = 'abcdefghijklmnopqrstuvwxyz'
    string =''
    for _ in range(nb):
        a = str(all[randint(0,26)])
        if a not in string:
            string += a
    return string

def position(char):
    for i in range(len(computer_hang)):
        if char == computer_hang[i]:
            position = computer_hang.index(char)
    return position

def printPos(pos):
    final ='-'*len(computer_hang)
    for i in range(len(computer_hang)):
        if (computer_hang.index(i) == pos):
            final[i] = computer_hang[i]
    print(final)
