# -*- coding: utf-8 -*-

#add elements from tropical and thisset into newset
thisset = {"apple","banana"}
tropical = {"cheery","mango"}
thisset.update(tropical)
print(thisset)

# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


#remove banana by using the discard() method
thisset = {"mango","apple","banana"}
thisset.discard("banana")
print(thisset)


# Remove the last item by using the pop() method:
thisset = {"apple","banana","cheery"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:
thisset = {"apple","banana","cheery"}
thisset.clear()
print(thisset)