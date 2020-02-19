
import random

# List comprehensions

minliste=[i for i in range(5)]  #simpel
print(minliste)

minliste=[i for i in range(50) if i%7==0]  #kondition. syvtabel
print(minliste)

minliste=[i for i in range(3,8)]  #anden range
print(minliste)

minliste=[i*i for i in range(3,8)]  #funktion 
print(minliste)

minliste2=[i+3 for i in minliste] # funktion af anden liste
print(minliste2)


def PlusRandom(a):
  return a +random.randint(0,9)

minliste3=[PlusRandom(i) for i in minliste] #egen funktion og egne liste
print(minliste3)


##NB kan bruges til mange listemanipulationer
testliste=[[1,3,5,7],[2,5,9,14],[3,6,8,11]]
print(testliste)
minliste4=[[float(y) for y in linie] for linie in testliste]  #konvertere integerliste til float
print(minliste4)


testliste5=[[y for y in line] for line in testliste if line[0]==1] #Her medtages kun linier hvor kolonne0=1
print(testliste5)

def Logik1(a): 
  if a==3:
    OK=True
  else:
    OK=False
  return OK

def Logik2(a,b,linie):
  if linie[a]==2 and linie[b]==5:
    OK=True
  else:
    OK=False
  return OK
  

#Kriterier
testliste5=[[y for y in line] for line in testliste if Logik1(line[0])] #Her medtages kun linier der hvor logik er sand
print("test5",testliste5)

testliste5=[[y for y in line] for line in testliste if Logik2(0,1,line)] #Kriterie med flere kolonner.overfører liste
print(testliste5)


antalkolonner=len(testliste[0])
antalraekker=len(testliste)
print(antalkolonner, antalraekker)

# Liste med sum af linier
testliste7=[[sum(line) for line in testliste]] #sum tager en liste som argument
print(testliste7)

# Sum af specifik  søjle (her søjle 0)
minsum=sum([line[0] for line in testliste])  #sum tager en liste som argument
print(minsum)

#transponer
testliste6=[[line[i] for line in testliste] for i in range(0,antalkolonner)]
print(testliste6)

#summer er så liniesum af den transponerede
kolonnesummer = [sum([line[i] for line in testliste]) for i in range(antalkolonner)] # Giver en liste med summer
print(kolonnesummer)
