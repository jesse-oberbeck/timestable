#!/usr/bin/env python3

import sys

if len(sys.argv) > 2:
	userIn = sys.argv[1]
	userOut = sys.argv[2]

else:
	userIn = input("Enter the name of the input file: ")
	userOut = input("Enter the name of the output file: ")

try:
	inFile = open(userIn,'r')
	outFile = open(userOut,'w')
except OSError:
	print("File operation failed. Closing Application.")
	exit()

line = inFile.readline()
while line:
	outFile.write(line)
	line = inFile.readline()
