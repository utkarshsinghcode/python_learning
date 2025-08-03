def myfunc(n):
    return abs(n - 50)  #abs kisi bhi no.       ka positive version deta hai. 
    # when we need diff. we use abs 


thislist = [100,50,65,82,23]
thislist.sort(key = myfunc) 
# key = myfunc ka mltb hai ki jb thislist sort ho woh mere func ko solve kare.


print(thislist)
