#!/usr/bin/env python

#Guess The Number Project
#Rorounifix
#Version 1.0

from random import randint
from pySys import *


def guess(answer):
    #print(answer)

    try:
        
        while True:
            guess = raw_input("Guess the Number 0 to 10 or 'q' to Quit: ")


            if(guess == "q" or guess == "quit" or guess == "Quit" or guess == "Q"):
                print("Quit!!!")
                return True
            elif(int(guess) == answer):
                clear()
                deco()
                print("Correct\n")
                cont()
                return True
            else:
                clear()
                deco()
                print("Wrong! Guess again ?\n")
    except:
        clear()
        deco()
        print('Try to put a Valid Number\n')
        cont()




def cont(): #continue
   
    x = raw_input("You want to Guess another Number? Y or N: ")
    if(x == "Y" or x == "y"):
        clear()
        deco()
        guess(randint(0,10))
    elif(x == "N" or x == "n"):
        print("Thanks !!! ;)")
    elif(len(x) >= 0):
        clear()
        deco()
        print("Y or N only\n")
        cont()


        
def deco():
    clear()
    print("===========================")
    print("#Guess The Number Project")
    print("#Rorounifix")
    print("#Version 1.0")
    print("===========================")
    print("\n")
    



if __name__ == "__main__":
    deco()
    guess(randint(0,10))
    
