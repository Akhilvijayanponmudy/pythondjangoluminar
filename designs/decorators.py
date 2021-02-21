
def subtract(func):
    def inner(num1,num2):  #10,20
        if num1 < num2:    #10<20
            (num1,num2) =(num2,num1)    #20,10
        return func(num1,num2)
    return inner


@subtract
def sub(num1,num2):
    return num1-num2


data=sub(10,20)
print(data)
