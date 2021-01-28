employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"arun","salary":35000,"exp":2},
    1002:{"id":1002,"name":"jack","salary":30000,"exp":2},
    1003:{"id":1003,"name":"jhon","salary":35000,"exp":2},
}

print(employee[1000])
#====================

#print 1001, name of employee
if(1001 in employee):
    print(employee[1001]["name"])
else:
    print("Employee with id not exist")
#======================================


#salary of 1003


if(1003 in employee):
    print(employee[1003]["salary"])
else:
    print("employee with id not exist")
#========================================

def employe_name(id=None):
    if(id in employee):
        print(employee[id]["name"])
    else:
        print("employenwith this id not found")

employe_name(1000)

#================================================

def print_employee(**kwargs):
    #print(kwargs)

    id=kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass
    else:
        print("employee with thid id not exist")




print_employee(id=1000,prop="exp")

#===============================================

