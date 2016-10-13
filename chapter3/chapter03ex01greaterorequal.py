#!/usr/bin/env python3

firstNumber = int(input("Number: "))
secondNumber = int(input("Next Number: "))

if firstNumber > secondNumber:
    print(firstNumber)
if secondNumber > firstNumber:
    print(secondNumber)
if firstNumber == secondNumber:
    print("Equal.")