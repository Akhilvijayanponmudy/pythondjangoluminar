f=open("movies.csv")

dict={}
for mov in f:
    data=mov.rstrip("\n").split(",")
    movies=data[1]
    year=data[2]

    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
for k,v in dict.items():
    print(k,"===>",v)
res=sorted(dict,key=dict.get,reverse=True)
print(res[0],"=========>",dict.get(res[0]))
#print(sorted(dict.items(),key=lambda kv:kv[1],reverse=True))