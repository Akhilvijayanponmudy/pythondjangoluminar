#class
#object
#reference


class person:
    #methods
    def setPerson(self,age,name):
        self.age=age
        self.name=name

    def print(self):
        print("name=",self.name)
        print("age=",self.age)
#we created a class person(set.nmae,set.age
#setPersdon()
#printPerson()

#object>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

obj=person()
obj.setPerson(25,"ajay")
obj.print()