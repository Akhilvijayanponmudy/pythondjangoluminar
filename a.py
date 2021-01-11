low=int(input("Enter Lower Limit"))
upp=int(input("Enter Upper Limit"))
flag=0
for i in range(low,upp+1):
    num=low%10
    if (num%10==0):
        flag+=1
        break
    else:
        flag=0
        if(flag==0):
            print(num)