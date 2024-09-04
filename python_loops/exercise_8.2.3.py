# -*- coding: utf-8 -*-

sentence = input("Enter a sentence: ")
counts = {}
for word in sentence.split():
   if word in counts:
       counts[word] = counts[word] + 1
     
   else:
        counts[word] = 1
        
print()
for word, count in counts.items():
   if count == 1:
       print(word, "appears once in the sentence")
   else:
       print(word,"appears",count,"times in the sentence")