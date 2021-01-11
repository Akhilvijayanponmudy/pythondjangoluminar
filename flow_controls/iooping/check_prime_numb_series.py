lownum=int(input("Enter Lower Limit"))
uppnum=int(input("Enter Upper Number"))


for num in range(lownum,(uppnum+1)):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=flag+1
            break
        else:
            flag=0
    if flag==0:
        print(num)

