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
