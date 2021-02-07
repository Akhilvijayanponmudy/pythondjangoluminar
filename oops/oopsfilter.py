class Employee:
    def __init__(self,eid,name,desig,exp,salary):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name


emplist=[]
f=open("employees","r")
for lines in f:
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employee(eid,name,desig,exp,salary))


devop=list(filter(lambda emp:emp.desig=="developer",emplist))
for emp in devop:
    print(emp)


cnt=len(list(filter(lambda emp:emp.desig=="developer",emplist)))
print(cnt)





maxsal=max(list(map(lambda emo:emo.salary,emplist)))
print(maxsal)