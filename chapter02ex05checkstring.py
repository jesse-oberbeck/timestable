#!/usr/bin/env python3
userString = input("Gimme a statment: ")
if userString.endswith("."):
    print("Yup, there's a period.")
else:
    print("No period.")
    
if userString.isalpha():
    print("All letters.")
else: 
    print("Something's not a letter.")

if "x" in userString:
    print("Gots a x!")
else:
    print("No x...")

if "e" in userString:
    modString = userString.replace("e", "E")
    print(modString)