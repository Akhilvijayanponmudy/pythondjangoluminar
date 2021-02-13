lst=[10,20,30,40]
lst2=[[10,20],[30,40],[50,60]]


squres=[num**2 for num in lst]
print(squres)


op=[num for ls in lst2 for num in ls]
print(op)