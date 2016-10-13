#!/usr/bin/env 

def mainloop():
	while True:
		accumulator = 0
		try:

			try:
				userInput = input("Enter an integer: ")

			except ValueError:
				print("Entry must be an integer.")

			if userInput == "end":
				exit()

			else:
				accumulator += userInput

		except EOFError:
			print("Shutting down.")

try:
	mainloop()
except (KeyboardInterrupt):
	print("Goodbye.")
	
