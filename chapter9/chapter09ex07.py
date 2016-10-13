#!/usr/bin/env python3

file1 = open('names_a.txt', 'r')
file2 = open('names_d.txt', 'r')
set1 = set()
set2 = set()


data = file1.readline()
while data:
	set1.add(data.rstrip("\n"))
	data = file1.readline()

data = file2.readline()
while data:
	set2.add(data.rstrip("\n"))
	data = file2.readline()

intersect = set1.intersection(set2)
print(intersect)
