class Bank:
    def balenq(self):
        print("inside balance enquiry")

    def withdraw(self):
        print("inside withdraw")

    def __deposit(self):         #>>>>>>>>>>>>private method
        print("inside deposit")

class Atm(Bank):
    pass

atm=Atm()
atm.withdraw()
atm.balenq()
#atm.deposit()   #not simply callable

obj=Bank()
obj._Bank__deposit()