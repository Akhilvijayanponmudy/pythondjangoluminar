num1=int(input("Enter NUmber1:"))
num2=int(input("Enter Number 2:"))

try:
    res=num1/num2
    print("Result=",res)
except Exception as e:
    print(e.args)


