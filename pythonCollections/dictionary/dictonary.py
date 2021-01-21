expenses={"jan":30000,"feb":25000,"march":28000}
print(expenses["jan"])




#values stored in dict in the form of key value
#how do we fetch value from dictnort
#is to pooible to store duplicate key, key must unique
#check for june20
print("june20" in expenses)


#adding new key value pairs
#june20:25000
expenses["june20"]=25000
print(expenses)



#substract

expenses["march"]-=3000
print(expenses["march"])
