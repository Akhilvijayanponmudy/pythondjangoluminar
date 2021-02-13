from re import *

#pattern="[a-z]"  #will check for lower case a to z
#pattern='[a-zA-Z]'
#pattern='[0-9]'
#pattern='[^0-9]   except 0 to 9
pattern='[^a-zA-z0-9]'



matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start())
    print(match.group())