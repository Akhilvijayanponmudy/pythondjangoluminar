lst=[10,8,11,7,12,6,5,9]
lst.sort()
low=0
upp=len(lst)-1
flag=0
element=int(input("Enter element you want to search"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if(flag==0):
    print("Element nof found")
else:
    print("Element found")
