#adding keys to dict.
#get method and get keys

car = {
     "brand": "suzuki",
     "model": "g_wagnor",
     "year": "2001"
}
x = car.get("model")
y = car.keys()
print(x)
print(y)

car["color"] = "grey"


print(y)
print(car)
      #new code#
#updating values method

car = {
    "brand": "konggolia",
    "model": "lambo",
    "color": "red"
}

x = car.values()
print(x)

car["year"] = 2024
print(x)
          #new code#
#get items method

car = {
    "brand": "konggolia",
    "model": "lambo",
    "color": "red"
}

x = car.items()
print(x)
          #new code#
#check if key exists

car = {
    "brand": "konggolia",
    "model": "lambo",
    "color": "red"
}

if "model" in car:
        print("yes,'model' is key")
      # new code#
#changing  values in dict.

car = {
    "brand": "konggolia",
    "model": "lambo",
    "color": "red"
}

car["brand"] = "volkswogan"
print(car)

#update dictionary

car1 = {
      "brand": "brezza",
      "model": "v6",
      "year":  2023
}

car1.update({"year": 2025})
print(car1)
        #new code#
#adding items to dict.

khet = {
      "fruits": "orange",
      "vitamim": "vit.c",
      "found":  "india"
}

khet["soil"] = "black"
print(khet)
        #new code#
# copy a  dict. to new one

car = {
    "brand": "suzuki",
    "model": "fronx",
    "year":  2023
}

mydict = car.copy()
print(mydict)
         #new code#
#nested dictionaries

myfam = {
     "child1": {
     "name": "raju",
     "year": 2004
     },
     "child2": {
     "name": "shyam",
     "year": 2007,
     },
     "child3": {
     "name": "baburav",
     "year": 2011
     }
}

print(myfam) 

#new code#
#creating 3 dict. and  inserting in 1.

child1 = {
     "name": "raju",
     "year": 2004
}
child2 = {     
    
     "name": "shyam",
     "year": 2007,
}
child3 = {     
     "name": "baburav",
     "year": 2011
}

myfamily = {
     "child1": child1,
     "child2": child2,
     "child3": child3,
}
print(myfamily)
    #new code#
#the concept of IF,ELIF,ELSE.

a = 2000
b = 2000
if a>b :
    print("a is greater")
elif b>a:
    print("b is greater")
else:
    print("both are EQUAL")

       #new code#
#the concept of IF,ELIF,ELSE.
# and logical concept
a = 201
b = 200
c = 2003

if a>b and c>a:
     print("both are TRUE")
     
# or logical concept

if a>b  or a>c:
     print("one is TRUE")
     
# NOT logical concept

if not a>b:
     print("a is not greater")
else:
    print("computer is fool")
