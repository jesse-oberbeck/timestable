#!/usr/bin/env python3
sortedlist = []
uniqueset = set()
countdic = {}
occurencelist = []
templist = []
while True:
    data = input("Enter text ('end' will quit) : ")
    uniqueset.add(data)
    
    if data == "end":
        for item in uniqueset:
            if " " in item:
                item = item.split(" ")
                for subitem in item:
                    if (subitem == " ") or (subitem == ""):
                        break
                    subitem = subitem.lower()
                    if subitem not in countdic:
                        
                        sortedlist.append(subitem)
                        countdic[subitem] = 1
                    else:
                        countdic[subitem] += 1
            else:
                if item not in countdic:
                    subitem = item.lower()
                    sortedlist.append(item)
                    countdic[subitem] = 1
                else:
                        countdic[subitem] += 1
        sortedlist.sort()
        for item in sorted(countdic, key=countdic.get, reverse=False):
            occurencelist.append([item,countdic[item]])
        print("\nSorted by word: ",sortedlist)
        #print(countdic)
        print("Sorted by occurences: ",occurencelist)
        break