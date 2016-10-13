#!/usr/bin/env python3

numdic = {'one':1,'two':2,'three':3}

def dictadd(numdic,num):
	for key in numdic.keys():
		numdic[key] += num

dictadd(numdic,3)
print(numdic)
