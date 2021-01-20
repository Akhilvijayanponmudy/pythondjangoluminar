lst=list()
limit=int(input("Enter how many number wants to upload:"))

for n in range(0,limit):
    number=int(input("Enter number"))
    lst.append(number)


tot=sum(lst)
res=list()

for i in lst:
    res.append(tot-i)
print(res)
