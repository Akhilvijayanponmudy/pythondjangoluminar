number=int(input("Enter Number:"))
6

lst=[1,5,4,3,8,2,6,9,7]
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==number):
            print(lst[i],lst[j])
