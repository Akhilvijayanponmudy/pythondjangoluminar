number=int(input("Enter Number"))
flag=0
if number==1:
    print("NOT Prime")
else:
    for i in range(2,number):
        if (number%2==0):
            flag=flag+1
            break
        else:
            flag=0
    if flag==0:
        print("Prime")
    else:
        print("Not Prime")