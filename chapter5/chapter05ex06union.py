#!/usr/bin/env python3

def theUnion(list1, list2):
	list1 = set(list1)
	list2 = set(list2)
	list1 = list(list1.union(list2))
	return list1

list1 = [1,2,3,4,5,6]
list2 = [1,2,4,6,8,10]
print(theUnion(list1,list2))

