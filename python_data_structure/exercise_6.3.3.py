# -*- coding: utf-8 -*-

#the union() method returns a new set with all the elements from both sets
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

#return a set that contains both items from sets x and y 
x = {"apple","mango","bnana"}
y = {"bnana","apple","cheery"}
z = x.intersection(y)
print(z)

# Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)