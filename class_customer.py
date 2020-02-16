
class Kunde(object):
    database = []

     
    
    def __init__(self, kundenummer, navn, volumen, marked):
        self.database.append(self)
        self.kundenummer = kundenummer
        self.navn = navn
        self.volumen=volumen
        self.marked=marked
        self.ordrer=[] #ordre er dato, volumen, pris
        self.saldo=0

    def findkunde(self,tekst):
        if self.navn.find(tekst)!=-1: print(self.navn)

    def visdata(self):
        print("Kundenummer: ",self.kundenummer,"Navn: ", self.navn,"Volumen: ", self.volumen,"Marked: ", self.marked)

    def betaling(self, betalt):
        self.saldo+=betalt

    def ordre(self,dato,ton, pris):
        self.saldo+=-pris
        self.volumen+=ton
        self.ordrer.append([dato,ton,pris])
        print(self.saldo,self.volumen,self.ordrer)

Novo=Kunde(123,"Novozymes",21000,"Miljø")
Weber=Kunde(124,"Saint Gobain Weber",12000,"Bygning")

#Her udlæses data fra en klasse
for x in Kunde.database : x.visdata()

antal=3

# Kunde er enkeltlinier per kunde
kunde=[0 for i in range(antal)]
kunde[0]=["Hofor",125,"Hovedstadens forsyning",10000,"Miljø"]
kunde[1]=["SR",126,"SR Gruppen",17000,"Road"]
kunde[2]=["Wewer",127,"Wewers mørtel",2300,"Bygning"]

# Kundeliste er et 2D array med alle kunder.
kundeliste=[[kunde[i][j] for j in range(5)]for i in range(antal)]

#Her laves class instances fra en liste(database)
for i in range(antal):
    kunde[i][0]=Kunde(kunde[i][1],kunde[i][2],kunde[i][3],kunde[i][4])

#Her udlæses opdaterede data fra klassen
for x in Kunde.database : x.visdata()

#Her finder vi kunder der indeholder teksten "ov"
for x in Kunde.database : x.findkunde("ov")

print(Novo.saldo, Novo.volumen,Novo.ordrer)
Novo.ordre("010218",200,150000)
Novo.ordre("050318",50,55000)
print(Novo.saldo, Novo.volumen,Novo.ordrer)
Novo.betaling(90000)
Novo.betaling(55000)
print(Novo.saldo, Novo.volumen,Novo.ordrer)
