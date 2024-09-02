# -*- coding: utf-8 -*-

# Get the value of the "model" key

# Get the value of the "model" key
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)
# Get a list of the keys:
x = thisdict.keys()
print(x)
# Get a list of the values:
x = thisdict.values()
print(x)

#add a new item to the original dictionary, and see that the keys list get updated as well
car = {
    "brand":"ford",
    "mode": "mustang",
    "year": 1999
    }
x = car.values()
print(x)
car["year"] = 2004
print(x)