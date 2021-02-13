from re import *

ph=input("Enter phone number")

rule='(91)?\d{10}'

matcher=fullmatch(rule,ph)

if matcher==None:
    print("Invalid phone number")
else:
    print("valid phone number")