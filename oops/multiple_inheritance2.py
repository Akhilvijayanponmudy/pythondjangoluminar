class Parent:
    def m1(self):
        print("inside perent")


class Child:
    def m1(self):
        print("inside child")

class SubChild(Child,Parent):
    def m3(self):
        print("inside sub child")

obj=SubChild()

obj.m1()

