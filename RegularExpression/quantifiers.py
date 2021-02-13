from re import *

#pattern="a+"         #any number of a excluding 0 number of a
#pattern="a*"          #any number of including 0 number
#pattern="a?"
#pattern="a{2}"
pattern="a{2,4}"


matcher=finditer(pattern,"aaaaaabaabaabaa")
for match in matcher:
    print(match.start(),"=>",match.group())
