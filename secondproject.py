#!/usr/bin/env python3

import random

#COUNT INVALID GUESSES?
count = 0
answer = 3#random.randrange(1,101)
lieUsed = False

def validate(guess):
	"""Takes the user's guess and checks if it is a valid,
	natural number."""
	try:
		guess = int(guess)
	except:
		print(guess, "is not a valid guess -", end=" ")
		return False
	return guess

def compareAnswer(guess):
	"""Gives the player information on whether
	their guess was higher or lower than the
	randomly generated correct answer"""
	if guess > answer:
		print(guess, "is too high -", end=" ")
	elif guess < answer:
		print(guess, "is too low -", end=" ")

def ulamsLie(guess):
	"""Gives the player incorrect information on 
	whether their guess was higher or lower than the
	randomly generated correct answer"""
	if guess < answer:
		print(guess, "is too high -", end=" ")
	elif guess > answer:
		print(guess, "is too low -", end=" ")
	

print("I'm thinking of a number between 1 and 100.")
guess = input("Try to guess my number: ")

while True:
	validate(guess)
	compareAnswer(guess)
	count += 1
	if guess == answer:
		print(guess, "is correct! You guessed my number in",\
		      count, "guesses.")
		break

	else:
		guess = validate(input("please guess again: "))
		if not lieUsed:
			lieChance = random.randrange(1,5)
			if lieChance == 3:
				ulamsLie(guess)
		compareAnswer(guess)
