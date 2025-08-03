def myfunc(n):
    return abs(n - 50)  #abs kisi bhi no.       ka positive version deta hai. 
    # when we need diff. we use abs 


thislist = [100,50,65,82,23]
thislist.sort(key = myfunc) 
# key = myfunc ka mltb hai ki jb thislist sort ho woh mere func ko solve kare.


print(thislist)
       #new code#
# add items to tuples

x = ("apple", "banana", "cherry")
y = list(x) #convert tuple to list

y.append("pine") #add items to list use append

x = tuple(y) #convert back to tupleand print

print(x) 
       #new code#
# remove items from tuples

x = ("apple", "banana", "cherry", "pine")
y = list(x) #convert tuple to list

#remove items to list use remove()method
y.remove("pine")

x = tuple(y) #convert back to tupleand print

print(x)
