#!/usr/bin/env python3
numlist = []
while True:
    data = input("Enter a number, or 'end' to quit: ")
    if data == "end":
        break
    else: 
        numlist.append(int(data))
        print(numlist)