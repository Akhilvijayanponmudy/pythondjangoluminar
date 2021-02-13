years=[
    {"id":10,"name":"christy","desig":"dataanalyst","sal":50000,"join":1980,"resign":1992},
    {"id":11, "name": "sabir", "desig": "developer", "sal": 54000, "join": 1985, "resign": 1990},
    {"id": 12, "name": "chris", "desig": "developer", "sal": 30000, "join": 1989, "resign": 1995},
]



#find highest salary
#print employee names whose exp >10 years
#

isl_2019=[
    {"team":"mumbaicity","mp":15,"won":10,"drawn":2,"loss":2,}
]


#find highest point teams
from functools import reduce
#                    listing team's points                 finding highest point
point_high=list(filter(lambda team:team["points"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["points"],isl_2019))),isl_2019)
print(point_high)



