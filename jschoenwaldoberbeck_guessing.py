#!/usr/bin/env python3

import random

answer = random.randrange(1, 101)  #Generates the answer on launch.
lieUsed = False  #Flag for the one time lie.
lieInfo = ""  #Placeholder string for lie output.

def validate(guess):
    """Takes the user's guess and checks if it is a valid,
    natural number between 1 and 100. Returns bool if
    invalid, else returns int.
    """
    try:
        assert not guess.startswith("0")
        guess = int(guess)
        assert guess >= 1 and guess <= 100 
    except:
        print(guess, "is not a valid guess -", end=" ")
        return False
    return guess

def compareAnswer(guess, truth):
    """Gives the player information on 
    whether their guess was higher or lower
    than the randomly generated correct answer.
    Has a chance to lie once. Returns a tuple.
    """
    high = "is too high -"
    low = "is too low - "
    position = "" #only really used for a lie
    if not truth:
        low, high = high, low  #Switches statements for lie.
    if guess > answer:
        print(guess, high, end=" ")
        position = "low"
    elif guess < answer:
        print(guess, low, end=" ")
        position = "high"
    return (guess, position)


#Initial prompt, and checks for validity and relative position to
#correct answer.    
print("I'm thinking of a number between 1 and 100.")
guess = input("Try to guess my number: ")
guess = validate(guess)
count = 0
if guess:
    compareAnswer(guess, True)
    count += 1

#All subsequent guesses. Loops until answer is true. During the loop,
#if the guess is incorrect, validity is checked, a decision is made
#regarding whether or not a one time lie is to occur, and the guess 
#is checked for relative position to answer.
#Truthfullness will depend on the previous check.
while True:
    if guess == answer:
        print(guess, "is correct! You guessed my number in",\
              count, "guesses.", lieInfo)
        break

    else:
        guess = validate(input("please guess again: "))
        if (guess and not lieUsed):
            count += 1
            lieChance = random.randrange(1, 5)
            if (lieChance == 3) and (guess != answer):  #Decision on lying.
                lie = compareAnswer(guess, False)
                lieInfo = "I lied about " + str(lie[0]) \
                      + " being too " + lie[1] + "."
                lieUsed = True  #Sets flag to not lie again.
            else:
                compareAnswer(guess, True)
        elif guess:
            count += 1
            compareAnswer(guess, True)
        else:
            pass
