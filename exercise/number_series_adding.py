num=input("Entert Number")
lim=int(num)+1
temp=0
res=0


for i in range(1,lim):
    temp=i*num
    res=int(temp)+res
print(res)