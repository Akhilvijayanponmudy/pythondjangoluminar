lst=[1,2,3,4,5,6]

numlist=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(numlist)



numlist2=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(numlist2)
