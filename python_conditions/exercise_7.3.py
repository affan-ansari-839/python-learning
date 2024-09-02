# -*- coding: utf-8 -*-

# nested if
#you can have if statments inside if statments, this is called nasted if statments
x = 4
if x > 10:
   print("Above Ten")
if x >20:
    print("and also above 20")
else:
    print("but not above 20")
   
    
 # if statements cannot be empty, but if you for some reason have an if statement
# with no content, put in the pass statement to avoid getting an error
a = 33
b = 200
if b > a:
   pass  
