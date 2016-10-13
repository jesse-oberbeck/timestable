#!/usr/bin/env python3

	

def B(twonums):
	result = lambda twonums: twonums[0] + twonums[1]
	return result(twonums)

twonums = [2,3]
print(B(twonums))
