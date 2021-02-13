class Student:
    def __init__(self,name,clas,location,mark):
        self.name=name
        self.clas=clas
        self.location=location
        self.mark=mark
    def __str__(self):
        return self.name
lst=[]
loca=[]
f=open("class","r")

for lines in f:
    name,clas,location,mark=lines.rstrip("\n").split(",")
    lst.append(Student(name,clas,location,mark))

loca=list(filter(lambda loc:loc.location=="ponmudy",lst))
for i in loca:
    print(i)

