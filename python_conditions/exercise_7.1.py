# -*- coding: utf-8 -*-

  #if statment
a = 33
b = 49
  
  
if b>a :
   print("b is greater then a")
   #If statement, without indentation (will raise an error):
  
       
  # The elif keyword is pythons way of saying "if the previous conditions were not true,
# then try this condition".
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
    
    
# The else keyword catches anything which isn't caught by the preceding conditions    
a = 200
b = 33
if b > a:
    print("b is greater then a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater then b")