num=int(input("Enter Number"))
low=int(input("Enter LOwer LImit"))
upp=int(input("Enter Upper Limit"))
res=0


for i in range(1,num+1):
    res=i**2
    if(low<res)&(upp>res):
        print(i,":",res)