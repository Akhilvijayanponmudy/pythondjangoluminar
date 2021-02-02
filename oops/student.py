class Student:
    def set_Student(self,rol,cource,name):
        self.rol=rol
        self.cource=cource
        self.name=name


    def get_Student(self):
        print(self.rol,",",self.cource,",",self.name)

obj=Student()
obj.set_Student(1000,"django","akhil")
obj.get_Student()
#instance variables are prepared with self keyword


print(obj.cource)
print(obj.name)