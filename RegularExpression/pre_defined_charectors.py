from re import *

#pattern="\s"    #chech for space
#pattern="\d"    #check for digits
#pattern="\D"    #except digit
#pattern="\w"    #check for all words except special charactors
pattern="\W"     #except words


matcher=finditer(pattern,"abc _7ZK@c")
for match in matcher:
    print(match.start(),"=>",match.group())