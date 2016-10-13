#!/usr/bin/env python3
for num in range(0,50):
    num = str(num)
    if not num.endswith('9'):
        print('{:5}'.format(num), end=" ")
    else:print('{:5}'.format(num))