#Funktion der bytter om på søjler og rækker
#############################################
def bytte(s,data):
    # s er søjler og data er matrix der ønskes transponeret
    return [[linie[j] for linie in data] for j in range(0,s)]
#############################################


#Funktion. Printe matrix med r rækker og s søjler og b i bredde per kolonne
#############################################
def skrivmatrix(r,s,b,data):
     for i in range(0,r):
        print()
        for j in range(0,s):
            print(str(data[i][j]).rjust(b),end=" ")
            #rjust er antallet af cifre og højrejustering
#############################################

#Funktion. Sorterer matrix efter kolonne s order = True eller false 
#############################################
def sortermatrix(s,indmatrix,orden):
    udmatrix=sorted(indmatrix, key=lambda kolonne: kolonne[s],reverse=not(orden))
    return udmatrix 
#############################################

#Funktion. Plukke kolonne nr s fra matrix 
#############################################
def plukkolonne(s,indmatrix):
    plukmatrix=[linie[s] for linie in indmatrix]
    return plukmatrix
#############################################

#Funktion. Plukke flere kolonner fra matrix. hlikekolonner er en liste med de kolonner der skal plukkes
#############################################
def plukflerekolonner(kolonneliste,indmatrix):
    plukkeflerematrix=[]
    for s in kolonneliste:
        plukkeflerematrix.append(plukkolonne(s,indmatrix))
    return plukkeflerematrix
#############################################


raekker=5
soejler=5

minliste=[x**2 for x in range(1,raekker+1)]
print (minliste)

minliste1=[[x*y**2 for x in range(1,raekker+1)]for y in range(1,soejler+1)]
print (minliste1)

for linie in minliste1:
    print(linie)
        
skrivmatrix(5,5,3,minliste1)

print()
print()

# Her skiftes ikke række
[print(str(minliste1[i][j]).rjust(3),end=" ") for i in range(0,raekker) for j in range(0,soejler)]

print()
print()

#Bytte om på rækker og søjler
mintransponeret=[[linie[j] for linie in minliste1] for j in range(0,soejler)]
print (mintransponeret)

print()
print()

fornavne=['Jens','Hans', 'Børge', 'Kaj','Kurt','Adam','Peter','Ulrik']
efternavne=['Svendsen','Hald','Skov','Andersen', 'Ødegaard', 'Bennet','Surkål','Kartoffel']
point=[23,34,67,87,12,24,88,55]
by=['Viborg','Aalborg','Nykøbing', 'Randers', 'Svendborg','Skibby','Bulderby','Østerlars']
postnummer=[4566,3400,6790,2330,5400,4300,7800,8930]

MineData=[fornavne,efternavne,point,by,postnummer]
     
#Udskrive matrix
skrivmatrix(5,8,12,MineData)
        
#bytter søjler og rækker
MineDataTransp=bytte(8,MineData)

print()
print()

# Udskrive transponeret matrix
skrivmatrix(8,5,12,MineDataTransp)

print()
print()

#Sortere efter en kolonne
MineDataSorted=sorted(MineDataTransp, key=lambda kolonne: kolonne[2])

skrivmatrix(8,5,12,MineDataSorted)

print()
print()

#Sætte en ny kolonne på

Bil=['Audi','BMW','Peugeot','Toyota','Nissan','Chrysler','Ford','Ferrari']
MineData.append(Bil)
skrivmatrix(6,8,12,MineData)

print()
print()

MineDataTransp=bytte(8,MineData)
skrivmatrix(8,6,12,MineDataTransp)

nymatrix=sortermatrix(3,minliste1,False)
skrivmatrix(5,5,3,nymatrix)

print()
print()

plukmatrix=[linie[3] for linie in nymatrix]
print(plukmatrix)

print()
print()

plukmatrix1=plukkolonne(2,nymatrix)
print(plukmatrix1)

hvilkekolonner=[1,3,4]
plukkeflerematrix=[]
for s in hvilkekolonner:
    plukkeflerematrix.append(plukkolonne(s,nymatrix))
print()
print(plukkeflerematrix)

plukmatrixkolonner=plukflerekolonner(hvilkekolonner,nymatrix)
print()
print()
skrivmatrix(3,5,3,plukmatrixkolonner)
print()
print()
skrivmatrix(5,3,3,bytte(5,plukmatrixkolonner))
print()
print()

#sammenlign rækker
comparerow=nymatrix[2]

#tom række
coltom=[0 for i in range(5)]

#resultat i ny matrix
modifiedmatrix=nymatrix[:][:]
#Transponere, sætte ny række ind, transponere giver en ny søjle med nuller
modifiedtrans=bytte(5,modifiedmatrix)
modifiedtrans.append(coltom)
modifiedmatrix=bytte(5,modifiedtrans)

#hvis der er et match i linien sættes noget i sidste kolonne
count=-1
for line in nymatrix:
    count+=1
    if line==comparerow:
        print(line[0],' ',count)
        modifiedmatrix[count][5]=77
    else:
        print('nope')
print()
print()   
skrivmatrix(5,6,3,modifiedmatrix)
