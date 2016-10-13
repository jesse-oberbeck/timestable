#!/usr/bin/env python3

import sys

nameDict = {}

for fileName in sys.argv[1::]:
	activeFile = open(fileName, 'r')
	data = activeFile.readline().rstrip("\n")
	while data:
		if data in nameDict:
			nameDict[data] += 1
			data = activeFile.readline().rstrip("\n")
		else:
			nameDict[data] = 1
			data = activeFile.readline().rstrip("\n")

	activeFile.close()

for key in nameDict:
	print("{0:10}{1}".format(key, nameDict[key]))
