number=int(input("Enter Number"))
lower=int(input("Enter Lower NUmber"))
upper=int(input("Enter Upper Limit"))
for i in range(1,(upper+1)):
    if i**number in range(lower,upper):
        print (i)