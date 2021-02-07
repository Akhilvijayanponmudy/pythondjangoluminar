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


for employee in emplist:
    if employee.desig=="developer":

        print("developers:",employee)

sallist=[]

for employee in emplist:
    sallist.append(employee.salary)
print("highest salary:",max(sallist))

devsal=[]
for employee in emplist:
    if employee.desig=="developer":
        devsal.append(employee.salary)
print("developer lowest salary:",min(devsal))






