#!/usr/bin/env python3

firstNumber = int(input("lower Limit: "))
secondNumber = int(input("Upper Limit: "))
thirdNumber = int(input("Step: "))

for num in range(firstNumber, secondNumber, thirdNumber):
    print(num)