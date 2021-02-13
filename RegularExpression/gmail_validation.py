from re import *

email=input("enter mail id")

rule='[a-zA-Z.]*[\d]*@gmail.com'


matcher=fullmatch(rule,email)

if matcher==None:
    print("Invalid mail id")
else:
    print("valid mail id")