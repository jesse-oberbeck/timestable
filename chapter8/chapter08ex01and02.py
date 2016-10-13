#!/usr/bin/env python3

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def inputLoop():
	userInput = ""
	while True:
		userInput = input("Enter index for item, or end to stop. >")

		if userInput == "end":
			exit()

		try:
			userInput = int(userInput)

		except:
			print("Invalid entry. Must be an integer.")
			inputLoop()

		try:
			assert userInput >= 0
		except AssertionError:
			print("Input is lower than 0.")
			inputLoop()

		try:
			print(mylist[userInput])
		except:
			print("Nothing there, boss.")
			inputLoop()



inputLoop()
