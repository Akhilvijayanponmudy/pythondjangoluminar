class Bank:
    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):                #private method
        print("inside deposit")
    def mcall(self):
        self.__deposit()


b=Bank()
#b.withdraw()
b._Bank__deposit()