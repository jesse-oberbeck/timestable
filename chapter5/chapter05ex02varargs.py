#!/usr/bin/env python3

def varargs(*multiarg, num):
	returnList = []
	for item in multiarg[0]:
		if item > num:
			returnList.append(item)
	return returnList

numbers = [10, 80, -455, 1, 4, 6, 17]
print(varargs(numbers, num=5))
