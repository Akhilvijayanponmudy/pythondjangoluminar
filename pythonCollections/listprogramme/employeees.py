employees=[
    [10,"christy","dataanalyst",50000],
    [11,"john","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomas","developer",47000],
    [18,"jhonis","developer",32000],
]

#print number of employees of this compny
number_of_employees=len(employees)
print(number_of_employees)

#=====================================================

#print how much salary compny has to raise inmonth end
stot=0
for emp in employees:
    stot+=emp[3]
print(stot)

#======================================================

#print high salary
salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
hi_salary=max(salary_list)


for emp in employees:
    if(emp[3]==hi_salary):
        print(emp)

#======================================================

#print employee name who receives loewst salary whose designation=developer

de_min=min(salary_list)
for emp in employees:
    if(emp[2]=="developer")&(emp[3]==de_min):
        print(emp)















