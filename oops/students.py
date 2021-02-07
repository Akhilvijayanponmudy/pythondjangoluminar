class Students:
    def __init__(self,rol,name,cource,total):
        self.rol=rol
        self.name=name
        self.cource=cource
        self.total=total

    def __str__(self):
        return self.name
    



obj=Students(100,"akshay","django",140)
obj1=Students(1001,"akhil","mean",140)
obj2=Students(1002,"ashil","django",145)

slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)

for stud in slist:
    if (stud.cource=="django"):
        print(stud.name)

tot=0
for stud in slist:
    if stud.cource=="django":
        tot+=stud.total
        print(tot)





