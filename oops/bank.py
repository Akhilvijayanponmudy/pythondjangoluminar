#withdrawal,deposit,balanceenq,create accoiunt
from datetime import datetime
class Bank:
    bank_name="sbi" #>>>>>class level variable
    def create_account(self,acno,personname,balance):
        self.acno=acno
        self.personname=personname
        self.balance=balance


    def deposit(self,amount):
        self.balance+=amount

        print(Bank.bank_name,"your account",self.acno,"has been credited with amt",amount,"on",datetime.today(), "avalable balance:",self.balance)


    def Withdrawal(self,amount):
        if self.balance > amount:
            self.balance-=amount
            print(Bank.bank_name,"your account", self.acno, "has been debited with amt", amount,"on",datetime.today(),"avalable balance:", self.balance)


        else:
            print("transaction cancelled with error code")

    def Balance_enq(self,amount):
        print(self.balance)


obj=Bank()

obj.create_account(1000,"tom",3000)
obj.deposit(30000)



