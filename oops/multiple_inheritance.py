class Parent:
    def m1(self):
        print("inside perent")


    def new(self):
        print("hello")

class Child:
    def m2(self):
        print("inside child")

class SubChild(Child,Parent):
    def m3(self):
        print("inside sub child")

obj=SubChild()
obj.m3()
obj.m2()
obj.m1()
obj.new()
