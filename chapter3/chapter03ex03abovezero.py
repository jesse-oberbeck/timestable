#!/usr/bin/env python3

numbers = input("Numbers: ")

numbers = numbers.split()

for num in numbers:
    if int(num) <= 0:
        numbers.remove(num)
        
print(numbers)