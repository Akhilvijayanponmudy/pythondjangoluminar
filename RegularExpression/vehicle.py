#validate vehicle registration
#kl 06 aa 8663

from re import *

vehnum=input("Enter Vehicle Number")

rule='kl\d{2}[a-zA-Z]{2}\d{4}'

matcher=fullmatch(rule,vehnum)

if matcher==None:
    print("Invalid vehicle number")

else:
    print("valid vehicle number")
