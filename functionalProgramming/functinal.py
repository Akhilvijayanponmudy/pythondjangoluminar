def add (num1,num2):
    return num1+num2

#lamda function
#---------------


add=lambda num1,num2: num1+num2

print(add(100,200))


sub=lambda num1,num2: num1-num2

print(sub(10,20))

#cube of a number

cube=lambda num: num**3
print(cube(3))


#even
#----

even=lambda num: num%2==0

print(even(10))