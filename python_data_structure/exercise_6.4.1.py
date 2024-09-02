# -*- coding: utf-8 -*-

# creat and print a dictionary
thisdict = {
 "brand":"ford",
"model":"mustang",
"year": 1978   
 }
print(thisdict)

#duplicate value will overwrite existing values
thisdict = {
 "brand":"ford",
 "model":"mustang",
 "year" : 1999,
 "year" : 2000   
    }
print(thisdict)

# String, int, boolean, and list data types:
thisdict = {
"brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]
}
print(thisdict)

# nested way
child1 = {
  "name":"Ali",
  "year": 2000
   }

child2 = {
    "name": "Hamza",
    "year": 2003
 }
child3 = {
    "name": "Zayan",
    "year": 2009
    }
myfamily = {
    
   "child1": child1,
   "child2": child2,
   "child3": child3
     }
print(myfamily)