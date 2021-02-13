#exception handling keywords
#try, except, finally


#try=> doutful code try


num1=int(input())
num2=int(input())
try:
    res=num1/num2
    print("result:",res)
except Exception as e:
    print(e.args)

print("i have one database transaction")
print("i have file operation")