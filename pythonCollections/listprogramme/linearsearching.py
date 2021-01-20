lst=[10,11,12,13,14,15]
element=int(input("enter element u want to search"))
flag=0
for num in lst:
    if (num==element):
        flag+=1
        break
    else:
        pass
if (flag==0):
    print("There is no element")
else:
    print("Element found")
