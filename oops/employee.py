class Employee:
    def set_Employee(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary

    def get_Employee(self):
        print(self.id,",",self.name,",",self.desig,",",self.salary)


obj=Employee()
obj.set_Employee(1000,"Ajay","kakkanad",30000)
obj.get_Employee()

obj2=Employee()

obj2.set_Employee(1001,"rahul","kochi",40000)
obj2.get_Employee()




print(obj2.name)







