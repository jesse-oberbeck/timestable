#!/usr/bin/env python3

import sys

def linecount(f):
	lines = f.readlines()
	lineCount = len(lines)
	return lineCount	

def wordcount(fread):
	words = fread.split(" ")
	wordCount = len(words)
	return wordCount

def charactercount(fread):
	charCount = 0
	for char in fread:
		charCount += 1
	return charCount

def startCounts(arg):
	f = open(arg)
	fread = f.read()
	f.seek(0)
	values = (linecount(f),wordcount(fread),charactercount(fread))
	f.close()
	return values

lineCountList = []
wordCountList = []
charCountList = []
results = []

if sys.argv[1] == "-t":
	for argIndex in range(2,len(sys.argv)):
		print("\t",startCounts(sys.argv[argIndex]))
		results.append(startCounts(sys.argv[argIndex]))

	for resultsTuple in results:
		lineCountList.append(resultsTuple[0])
		wordCountList.append(resultsTuple[1])
		charCountList.append(resultsTuple[2])
	print("Totals: ",sum(lineCountList),sum(wordCountList),sum(charCountList))


else:
	for argIndex in range(1,len(sys.argv)):
		print(startCounts(sys.argv[argIndex]))

