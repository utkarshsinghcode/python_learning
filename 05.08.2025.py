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
