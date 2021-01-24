pattern="ABABBAC"
#find first recursive charactor A
dict={}

for ch in pattern:
    if (ch not in dict):
        dict[ch]=1
    else:
        print(ch,"recursive charactor")
        break