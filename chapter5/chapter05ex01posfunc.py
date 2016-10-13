#!/usr/bin/env python3

def returnpos(thelist):
	for item in thelist:
		if not item % 2 == 0:
			thelist.remove(item)
	return thelist

thelist = [1,2,3,4,5,6,7,8,9,10]
print(returnpos(thelist))
