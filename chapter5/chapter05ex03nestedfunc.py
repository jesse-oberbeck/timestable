#!/usr/bin/env python3


def A(first, second):
	final = first + second
	return final
def B(twonums):
	first = twonums[0]
	second = twonums[1]
	return A(first,second)

twonums = [2,3]
print(B(twonums))
