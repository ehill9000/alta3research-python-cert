#!/usr/bin/env python3

'''Author: Eric Hill | This script is to show my python skills for basic certification from alta3.'''

#Import built in random module
import random
#Import pip install crayons from PYPI
import crayons

def main():
    #Set initial value of Play Again to Y for Yes
    again = "Y"    
    highscore = 999
  
    #Continue to run game while again is Y
    while again.upper()  == "Y":
    #Tell the user what kind of game they are playing
        print("What number am I thinking of? (1-100)")
        #Set the number to a random number between 1 and 100
        number = random.randint(1,100)
        #Set the number of attempts at 0
        i = 0
        #Loop below script until user guesses number correctly
        while True:
            #Check if user is entering an int as number
            try:

                guess = int(input(">> "))
                #Increment number of attempts by +1 for each guess
                i += 1
            #If user enters a non int, display error
            except ValueError:
                print("Invalid Input")
                #Increment number of attempts by +1 even if user inputs non-int 
                i += 1
                #Repeat from start if user entered non-int
                continue
            #If the user enters a value higher than the random number, help them out and say too high
            if guess > number:
                print("Too high!")
            #If the user enters a value lower than the random number, help them out and say too low
            elif guess < number:
                print("Too Low!")
            #If the user enters the correct value matching the number they win
            elif guess == number:
                #Print in green the winning message. Display the winning number
                print(crayons.green("YOU WIN! Good Job! The number was"), str(number) +".")
                #Display to user how many tries it took to guess the right number
                print("It took you", i,"tries.")
                #Ask the user if they want to play again, if not, end the script
                print("Play again? Y=YES, ANYTHING ELSE=NO")
                again = input(">> ")
                break
main()
