num=int(input("Enter Number"))
rowcol=num+1
colrow=num-1
collim=num*2



for row in range(1,num+1):
    for col in range (1,collim):
        if (row==num) | (row+col==rowcol) | (col-row==colrow):
            print("*",end="")
        else:
            print(end=" ")
    print()