
testliste=[[1,3,5,7],[2,5,9,14],[3,6,8,11]]
print(testliste)

#Konvertere format
floatliste=[[float(i) for i in line] for line in testliste]
print(floatliste)

#Et kriterie
filterliste=[[i for i in line ] for line in testliste if line[0]==1]
print(filterliste)

#kriterie med and
kriterieliste=[[i for i in line] for line in testliste if line[0]==1 and line[2]==5]
print(kriterieliste)

#sum af linier
liniesumliste=[sum([i for i in line]) for line in testliste]
print(liniesumliste)

#transponere
col=len(testliste[0])
transponerliste=[[line[i] for line in testliste] for i in range(0,col)]
print(transponerliste)

# sum af kolonner = sum af linie i transponeret
sumkolliste=[sum([line[i] for line in testliste]) for i in range(0,col)]
print(sumkolliste)

# kvartal, kontonummer, tekst, beløb
regnskab=[[2,1200,"hej",35.5],[1,1300,"hej",35.5],[4,1200,"hej",222.9],[3,1200,"hej",473.2],[2,1200,"hej",20.5],[3,1300,"hej",75.8],[4,1300,"hej",355.6],[3,1200,"hej",125.0]]

#liste med kvartaler og kontonumre
kvartal=[1,2,3,4]
konto=[1200,1300]

kol=len(regnskab[0])
for q in kvartal:
  for k in konto:
    filterliste=[[i for i in line] for line in regnskab if line[0]==q and line[1]==k]
    sumafbeloeb=sum([line[3] for line in filterliste])
    print(q," ", k, sumafbeloeb)
  
