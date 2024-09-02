# -*- coding: utf-8 -*-

#using the append() method to append an item
thislist = ["apple","bnana","cherry"]
thislist.append("orange")
print(thislist)

#insert an item as second position
thislist = ["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)

#adding the elements of tropica to thislist
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
