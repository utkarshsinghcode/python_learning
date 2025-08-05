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
