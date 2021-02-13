num1=int(input("number1:"))
num2=int(input("number2:"))

try:
    res=num1/num2
    print(res)
except:
    num2=int(input("number 2:"))
    try:
        res=num1/num2
        print(res)
    except:
        num2=int(input("number 2:"))
        res=num1/num2
        print(res)

finally:
    print("i have database transaction")
    print("i have file operation")