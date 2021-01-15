lst=[10,11,12,13,14,15,16,17]
evenlst=list()
oddlst=list()
for num in lst:
    if(num%2==0):
        evenlst.append(num)
    else:
        oddlst.append(num)

totalodd=sum(evenlst)
totaleven=sum(oddlst)
print(evenlst)
print(oddlst)
print("Total of Odd numbers :",totalodd)
print("Total of Even Numbers:",totaleven)