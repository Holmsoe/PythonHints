
import time

def ikkelukke():
    #Denne metode lukker ikke fil automatisk og kræver en close
    Minfil = open('materialer1-csv.txt','r')
    print(Minfil.read())
    Minfil.close()

def withmetode():
    #Denne metode lukker automatisk når vi er ude af "with"
    with open('materialer1-csv.txt','r') as Minfil:
        #næste linie læses/skrives
        print(Minfil.readline())
        #næste 100 tegn læses/skrives
        print(Minfil.read(100))
    
        #Sådan får vi info om current position i fil
        print("Her er vi: ",Minfil.tell())
    
        #Sådan går vi til en bestemt position i fil
        print("Nu er vi tilbage til start: ", Minfil.seek(0))
        print("Forfra ")
        print(Minfil.read(100))

def stumper():
    #Metode til læsning i stumper
    with open('materialer1-csv.txt','r') as Minfil:
        stepRead=100
        stump=Minfil.read(stepRead)
        print("Vi læser hele filen i stumper")
        while len(stump)>0:
            print(stump,end="")
            stump=Minfil.read(stepRead)
            
def liniermedIterator():
    with open('materialer1-csv.txt','r') as Minfil:
        filliste=[line for line in Minfil]
        print("Antal linier med iterator: ",len(filliste))

def liniermedList():
    with open('materialer1-csv.txt','r') as Minfil:
        filliste1=list(Minfil)
        print("Antal linier med list: ",len(filliste1))
        print(filliste1)
            
def liniermedReadlines():
    with open('materialer1-csv.txt','r') as Minfil:
        filliste1=Minfil.readlines()
        #filliste1=list(Minfil)
        print("Antal linier med readlines: ",len(filliste1))

def splittelinie():
    #her tilhører ordene en list. Split giver en liste
    with open('materialer1-csv.txt','r') as Minfil:              
        for ord in Minfil.readline().split(","):
            print('{:10}'.format(ord)," ",end="") #right align

def linieforlinie():
    #Ingen liste
    with open('materialer1-csv.txt','r') as Minfil:              
        for line in Minfil:
            print("")
            for ord in line.split(","):
                print('{:10}'.format(ord)," ",end="") 
                #print(ord,end="")

#Funktion. Sorterer matrix efter kolonne s orden = True eller false 
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

#Funktion. Plukker flere kolonner fra matrix. hlikekolonner er en liste med de kolonner der skal plukkes
#############################################
def plukflerekolonner(kolonneliste,indmatrix):
    plukkeflerematrix=[]
    for s in kolonneliste:
        plukkeflerematrix.append(plukkolonne(s,indmatrix))
    return plukkeflerematrix
#############################################

#Funktion der bytter om på søjler og rækker
#############################################
def bytte(data):
    s=len(data[0])
    # s er søjler og data er matrix der ønskes transponeret
    return [[linie[j] for linie in data] for j in range(0,s)]
#############################################

#Funktion der printer tabel og afpasser kolonnebredde
#############################################
def maxkarak(datafil):
    minmatrix=[]
    colbredde=[]       
    for line in list(datafil): minmatrix.append(line.split(";"))
    transmatrix=bytte(minmatrix)
        
    for line in transmatrix:
        maxtext=0
        for element in line:
            if len(element)>maxtext: maxtext=len(element)
        colbredde.append(maxtext)

    for line in minmatrix:
        print("")
        lg=20
        for elementnr,element in enumerate(line):
            print('{:{bredde}}'.format(element,bredde=colbredde[elementnr]+2),end="")
#############################################
    
#ikkelukke()
#withmetode()
#stumper()  
#liniermedIterator()
#liniermedList()
#liniermedReadlines()
#splittelinie()
#linieforlinie()
    
#kolonnebredde()
with open('materialer.txt','r') as Minfil: 
    maxkarak(Minfil)
        
