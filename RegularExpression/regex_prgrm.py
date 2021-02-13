#regular expression (used to pattern matching)

#step 1 import re module
from re import *

pattern="ab"

matcher=finditer(pattern,"ababababababababababbbbabababa")
#                         0123456789   (position)
cnt=0
for match in matcher:
    print(match.start())  #return position       0    2    4    6....
    print(match.group())  #matching object      ab   ab    ab   ab...
    cnt+=1
print(cnt) #13 times occures


