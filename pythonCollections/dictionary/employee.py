employe={"id":100,"ename":"ajay","exp":2,"salary":35000}


if("salary" in employe):
    print(employe["salary"])

#print employee name
print(employe["ename"])

#check and gender

if("gender" in employe):
    print("Exist")
else:
    employe["gender"]="male"
print(employe)

#if employee salary<35000 add 5000 rupees more
if(employe["salary"]<=35000):
    employe["salary"]+=5000
print(employe)