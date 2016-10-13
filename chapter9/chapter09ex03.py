#!/usr/bin/env python3

userIn = input("Enter the name of the input file: ")
userOut = input("Enter the name of the output file: ")
inFile = open(userIn,'r')
outFile = open(userOut,'w')

line = inFile.readline()
while line:
	outFile.write(line)
	line = inFile.readline()
