#!/usr/bin/env python3

thelist = [10,40,30,20,5,392]

def sort(thelist):
	funclist = []
	for item in thelist:
		funclist.append(item)
	funclist.sort()
	return funclist

def reverse(thelist):
	funclist = []
	for item in thelist:
		funclist.append(item)
	funclist.reverse()
	return funclist

print(reverse(sort(thelist)))
print(thelist)


