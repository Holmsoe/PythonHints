def f(a,L):
    L.append(a)
    return L

start=1
stop=10
minliste1=[]

for i in range(start,stop):
    minliste1=f(i,minliste1)
    pass

start=11
stop=14
minliste2=[]

for i in range(start,stop):
    minliste2=f(i,minliste2)
    pass
print ('minliste1')
print(minliste1)
print ('minliste2 after append')
print(minliste2)

#merge to lister
minliste3=[3,4]
minliste3[len(minliste3):]=minliste1
print('merge lists')
print(minliste3)

#merge 3 lister
minliste4=[21,22]
minliste4.extend(minliste1)
minliste4.extend(minliste2)
print('merge lists with extend')
print(minliste4)

#Indsætter nyt led på plads nummer 6
minliste4.insert(6,'abe')
print('insert item')
print(minliste4)

#Fjerner forekomst af 6 og ikke 6. led
minliste4.remove(6)
print('remove item')
print(minliste4)

#fjerner et led og gemmer det
ud=minliste4.pop(7)
print('pull out item and save to variable')
print(minliste4)
print(ud)

#Hvilket index har værdien 11
nr=minliste4.index(11)
print('index of value in list')
print(nr)

#Antal forekomster af et led
antal=minliste4.count('abe')
print('number of incidents')
print(antal)

print('reverse list')
print(minliste4)
minliste4.reverse()
print(minliste4)

#Konverterer alle listens dele til string.
#Først gemmes leddet, så fjernes det og herefter indsætte stringversionen
for i in range(0,len(minliste4)):
    gem=minliste4[i]
    minliste4.remove(gem)
    minliste4.insert(i,str(gem))
print('convert list members to string')  
print(minliste4)    

#kan kun sortere på samme datatyper og ikke feks integer og string
print('sort list')
minliste4.insert(3,'urt')
print(minliste4)
minliste4.sort()
print(minliste4)
