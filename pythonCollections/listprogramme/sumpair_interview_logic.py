lst=[1,2,3,4]
lst.sort()
low=0
upp=len(lst)-1

element=int(input("Emter Element"))
while(low<upp):
    tot=lst[low]+lst[upp]
    if (element==tot):
        print(lst[low],lst[upp])
        break
    elif(element>tot):
        low+=1
    else:
        upp-=1