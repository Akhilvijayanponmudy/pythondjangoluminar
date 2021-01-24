f=open("demo","r")


word=[]

for lines in f:
    word.append(lines.split(" "))
print(word)


mywords=[]
for lst in word:
    for wrd in lst:
        mywords.append(wrd)
print(mywords)


