#!/usr/bin/env python3
sortedlist = []
uniqueset = set()
while True:
    data = input("Enter text ('end' will quit) : ")
    uniqueset.add(data)
    
    if data == "end":
        for item in uniqueset:
            if " " in item:
                item = item.split(" ")
                for subitem in item:
                    sortedlist.append(subitem.lower())
            else:
                sortedlist.append(item.lower())
        sortedlist.sort()
        print(sortedlist)
        break