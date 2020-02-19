
minlist=[[str(i)+str(j) for j in range(0,9)] for i in range (0,9)]
for i in range(0,1):
    for j in range(0,9):
        minlist[i][j]="a "

for i in range(0,1):
    for j in range(0,9):
        minlist[j][i]="b "       
        
print(minlist)
        
#husk at der er en række og søjle med nuller her
#I en list comprehension starter index altid med 0


for r in range(8,-1,-1):
    for s in range(0,9):
        if (s)%9==0: print("")
        print(minlist[r][s]," ",end="")

for r in minlist:
    for q in r:
        print

print("")
for i, e in reversed(list(enumerate(minlist))):
    for j, q in list(enumerate(e)):
        if j%9==0: print("")
        if i!=0 and j!=0: print(q," ",end="")

