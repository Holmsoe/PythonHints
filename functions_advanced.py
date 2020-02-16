
#=================
# Man kan assigne en variabel til en funktion.
#=================
def hej(navn):
    return "hej "+navn

#uden parameter
hejmeddig = hej
print (hejmeddig("John"))

#med parameter
hej2=hej("Finn")
print(hej2)

#=================
# Definere en funktion i en funktion.
#=================

#Bemærk at underfunktionerne kender parametre i hovedfunktion. 
def BeregnSumDivideretMedProdukt(a,b):
    x=a
    y=b
    def beregnsum():
        return a+b
    def beregnprodukt(a,b): #a,b er unødvendig
        return x*y

    result = beregnsum()/beregnprodukt(a,b)
    return result

#Direkte
print("Sum divideret med produkt",BeregnSumDivideretMedProdukt(3,5))

# Med variabel
minBeregning=BeregnSumDivideretMedProdukt

print("Sum divideret med produkt {0:2.3f}".format(minBeregning(3,5)))

#=================
# Kalde en funktion med en funktion som parameter.
#=================

def minpowerfunktion(a,p):
    ud=a**p
    return ud
def mingangefunktion(a,b):
    ud=a*b
    return ud
def mindividerfunktion(a,b):
    ud=a/b
    return ud
def minplusfunktion(a,b):
    ud=a+b
    return ud
def minminusfunktion(a,b):
    ud=a-b
    return ud

#Dette er ikke en del af eksempel med kald med funktion 
def minsumfunktion(*a):
    minsum=0
    for item in a:
        try:
            minsum+=item    # hvis a er et antal tal
        except:
            for tal in item:    # hvis a er lister eller tupler med tal
                minsum+=tal
    return minsum

print(minpowerfunktion(2,5))
n=12
print(minsumfunktion([i for i in range(n)]))    # sum af liste
print(minsumfunktion([i for i in range(n)],[i**2 for i in range(n)]))   #sum af to lister

def sumafpower(n,p):
    ListePower=[minpowerfunktion(a,p) for a in range(n+1)]
    resultat=minsumfunktion(ListePower)
    return resultat

print(sumafpower(5,2))
#Slut på det er ikke er relevant

#Nu kalder vi de forskellig funktioner fra en fælles kaldefunktion

def minkaldefunktion(a,b,funktion):
    ud=funktion(a,b)
    print("Hej fra kaldefunktion. Resultatet er: ",ud)
    return ud

minkaldefunktion(3,5,minpowerfunktion)
minkaldefunktion(3,5,minplusfunktion)

#=================
# Funktion med funktion som output.
#=================

def Beregn(p):
    def minsum(a,b):
        c=a+b
        print("Summen af {0} og {1} er: {2}".format(a,b,c))
    def mitprod(a,b):
        c=a*b
        print("Produktet af {0} og {1} er: {2}".format(a,b,c))

    valg={0:minsum,1:mitprod}
        
    return valg[p]
    
#Vi sætter nye funktioner som output af Beregn
MinSumfunktion=Beregn(0)
MinProduktfunktion=Beregn(1)
# Vi beregner ved hjælp af nye funktioner
MinSumfunktion(3,4)
MinProduktfunktion(3,4)
# Vi beregner direkte
Beregn(0)(3,4)
        

#=================
# Simpel decorator der tilføjer lidt tekst og ganger resultat med 2
#=================

# En decorator tager en funktion som argument.
# Den returnerer en anden funktion der afhænger af funktionen og dekoreringen i den indre funktion


def mindeco(funktion):
    def minwrapper(a,b): #Samme antal argumenter som oprindelig funktioner
        print("Jeg dekorerer lidt")
        ud = funktion(a,b)*2
        print("Funktionsresultat:{0} Decoresultat: {1}".format(funktion(a,b),ud))
        return ud
    return minwrapper

def funk1(a,b):
    return a+b
def funk2(a,b):
    return a*b

decofunktion1=mindeco(funk1)
decofunktion2=mindeco(funk2)

decofunktion1(32,11) #Kald gennem ny variabel der repræsenterer den dekorerede funktion.
mindeco(funk2)(4,7) #Direkte kald. Først defineres den dekorerede funktion. Så sættes parametre

#decorator med python syntax
@mindeco
def funk3(a,b):
    return a/b

funk3(45,9)
