from functools import reduce

lst=[10,11,12,13,14]


high=reduce(lambda no1,no2: no1 if no1>no2 else no2,lst)
print(high)



lowest=reduce(lambda no1,no2: no1 if no1<no2 else no2,lst)
print(lowest)

