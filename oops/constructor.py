#initrializing instanbce variables
#constructor name always class name...............in pythgon constructor name is __init

#constructor automatically invoked during object creation


class Student:
    def __init__(self,rol,cource,name):
        self.rol=rol
        self.cource=cource
        self.name=name
    def get_Student(self):
        print(self.rol,",",self.cource,",",self.name)


obj=Student(1001,"django","akhil")

print(obj.cource)
obj.get_Student()
