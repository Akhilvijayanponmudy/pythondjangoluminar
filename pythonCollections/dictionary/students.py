f=open("students","r")
students={}

for lines in f:
    id,name,total,cource=lines.rstrip("\n").split(",")


    if id not in students:
        students[id]={"id":id,"name":name,"total":total,"cource":cource,}



def print_students_data(**kwars):
    id=kwars["id"]
    if id in students:
        print(students[id]["name"])
        if "prop" in kwars:
            prop=kwars["prop"]
            print(students[id][prop])
    else:
        print("there is no student exits with thid id")
 #=======================================================




print_students_data(id="1001",prop="total")


