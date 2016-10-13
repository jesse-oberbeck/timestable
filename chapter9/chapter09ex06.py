#!/usr/bin/env python3

import os
import time

fileSize = input("Minimum file size: ")
dirItems = os.listdir()
for item in dirItems:
	stats = os.stat(item)

	print(item, "size: ", stats.st_size, time.ctime(stats.st_mtime),"\n")

