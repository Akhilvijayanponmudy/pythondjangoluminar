names=["india","pak","aus","eng","sa","srilanka","aukland","indonesia"]

upplist=list(map(lambda name:name.upper(),names))
print(upplist)


#starting with a


acountry=list(filter(lambda name:name[0]=="a",names))
print(acountry)