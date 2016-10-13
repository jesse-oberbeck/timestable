#!/usr/bin/env python3

import sys

def linecount(f):
	lines = f.readlines()
	lineCount = len(lines)
	return lineCount	

def wordcount(f):
	words = fread.split(" ")
	wordCount = len(words)
	return wordCount

def charactercount(f):
	charCount = 0
	for char in fread:
		charCount += 1
	return charCount

argList = []
for argFile in range(1,len(sys.argv)):
	argList.append(sys.argv[argFile])

for fileName in argList:
	f = open(fileName)
	fread = f.read()
	f.seek(0)
	print(linecount(f))
	print(wordcount(fread))
	print(charactercount(fread))
	f.close()


