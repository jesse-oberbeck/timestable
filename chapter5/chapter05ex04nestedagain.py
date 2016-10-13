#!/usr/bin/env python3


def A(first, second):
	final = first + second
	return final
def B():
	first = twonums[0]
	second = twonums[1]
	return A(first,second)

global twonums
twonums = [2,3]
print(B())
