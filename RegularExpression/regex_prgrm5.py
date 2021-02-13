#a,k first charactor must be an alphabet between a-k
#second must be a digit divisable by 3
#followed by any number of charactor


from re import *
varname=input("Enter Variable Name")

rule="[a-k][a-zA-Z0-9]*"




matcher=fullmatch(rule,varname)

if match==None:
    print("invalid variable name")
else:
    print("valid variable name")