#!/usr/bin/env python3

def mainloop():
	accumulator = 0
	while True:

		try:
			userInput = int(input("Enter an integer: "))

		except(ValueError):
			print("Entry must be an integer.")
		except(KeyboardInterrupt):
			print(" Caught Keyboard Interrupt!")
		except(EOFError):
			print("exiting...\nTotal:",accumulator)
			exit()

		if userInput == "end":
			exit()

		else:
			accumulator += userInput



mainloop()

