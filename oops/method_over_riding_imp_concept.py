class Parent:
    def mobile(self):
        print("Nokia5310")

class Child(Parent):
    def mobile(self):
        print("iphone11")


c=Child()
c.mobile()