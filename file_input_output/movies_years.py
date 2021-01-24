f=open("movies.csv")

dict={}
res={}
for mov in f:
    data=mov.rstrip("\n").split(",")
    movies=data[1]
    year=data[2]
    rating=data[3]
    if(movies not in dict):
        dict[movies]=year,rating
    else:
        pass
#for k,v in dict.items():
 #   print(k,"===>",v)

res=sorted(dict,key=dict.get,reverse=True)
print(res)
