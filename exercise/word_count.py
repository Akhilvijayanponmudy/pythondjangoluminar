f=open("words","r")
dict={}



for wrds in f:
    data=wrds.rstrip("\n").split(" ")
    for i in data:
        if(i not in dict):
            dict[i]=1
        else:
            dict[i]+=1
for k,v in dict.items():
    print(k,v)
res=sorted(dict,key=dict.get,reverse=True)
print(res)
print(res[0],dict.get(res[0]))