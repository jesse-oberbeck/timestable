#!/usr/bin/env python3

firstNumber = int(input("Number: "))
secondNumber = int(input("Next Number: "))

total = 0
for num in range(firstNumber, (secondNumber+1)):
    total += num
    
print(total)