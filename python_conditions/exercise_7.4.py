#!/usr/bin/env python3

print("Hello!")
word = input("Enter something; ")

if word == "hi":
    print("hi to yo too!")
else:
     if word == "hello":
         print("hello to you too")
     else:
         if word == "hey":
               print("Hey hey hey!")
         else:
             print("I don't know what", word ,"means.") 
             
             
             
# This code is a mess. We need to indent more every time we want to check for more words.
# Here we check for 5 different words, so we have 5 levels of indentation. If we would need to
# check 30 words, the code would become really wide and it would be hard to work with.
# Instead of typing else, indenting more and typing an if we can simply type elif,
# which is short for else if. Like this:
print("Hello!")
word = input("Enter something: ")
if word == "hi":
  print("Hi to you too!")
elif word == "hello":
  print("Hello hello!")
elif word == "howdy":
  print("Howdyyyy!")
elif word == "hey":
  print("Hey hey hey!")
elif word == "gday m8":
  print("Gday 4 u 2!")
else:
  print("I don't know what", word,"means.")
            
             