#polymorphism
#more than one form




#method overloading
#same method different number of arguments

class Maths:
    def add(self):
        print("inside no arg")

    def add(self,num1):
        print("inside one arg")

    def add(self,num1,num2):  #only this works
        print("inside two arg")


m=Maths
m.add(1)


#only recently added works