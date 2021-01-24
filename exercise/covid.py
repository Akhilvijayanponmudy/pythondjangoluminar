f=open("covid_19_india.csv","r")
dict={}


for item in f:
    data=item.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telangana"

    confirmed_cases=data[8]
    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,"====>",v)


res=sorted(dict,key=dict.get,reverse=True)
print(res)


