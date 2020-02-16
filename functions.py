
def plusf(*a):
    sumf=0
    for item in a:
        try:
            sumf+=item
        except:
            for tal in item:
                sumf+=tal
    return sumf

def prodf(*a):
    sumf=1
    for item in a:
        try:
            sumf*=item
        except:
            for tal in item:
                sumf*=tal
    return sumf


# Assign en variable til funktion. Funktion som parameter

minplus=plusf
print(minplus([3,4,5,6],[6,7,8]))

# Funktion indeni funktion

def ydrefunktion(a,b):
    def minsum():
        ud=a+b  #Indre funktion kender parametre i ydre funktion
        return ud
    def mitprod():
        ud=a*b  #Indre funktion kender parametre i ydre funktion
        return ud
    def mitsumprod():
        ud=minsum()*mitprod() # indre funktioner kan kaldes fra indre funktioner
        return ud
    
    print("Inden beregning")
    print(minsum()*mitprod())
    print(mitsumprod())

ydrefunktion(4,5)

#Funktioner kan returnere funktioner. Nyttig ved ligninger med parameter
#Ydre returnerer en funktion med variablen x. Når denne funktion kaldes beregnes først resultatet
def ydre(a):
    def indre(x):
        return a*x**2
    print("kald indre fra ydre",indre(5))
    return indre

minsammensatte=ydre(3)
print("kald via parameter i to steps",minsammensatte(5))
print("kald med begge parametre",ydre(3)(5))
      

