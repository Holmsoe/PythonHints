
#En liste er en række af elementer. Kan være forskellige typer.
#Men nogle funktioner såsom sum og sorter virker ikke hvis typerne er forskellige.

#En liste kan erklæres uden indhold med

listeA=[]
print(len(listeA))
# dette viser at listen har længden 0.

#En liste kan sættes direkte
listeB=['A','AB','ABC',1,2,3]
print('listeB')
print(listeB)

#Variable kan også indgå
var1='Mig '
var2='Dig'
var3='ViTo'
listeC=[var1,var2,' og',var3]
print('listeC')
print(listeC)

# En liste kan også sættes med et udtryk
# L = [expression for variable in sequence]
# expression er et udtryk der afhænger af variabel
# sequence definerer intervallet

listeD=[x**2 for x in range(0,22,2)]
# en liste af kvadrattal for lige tal i intervallet 1-20.
#Hust at sidste i sekven ikk er med.
print('listeD')
print(listeD)

# istedet for expression kan anvendes en funktion
def kvadrat(i):
    return i**2
listeE=[kvadrat(x) for x in range(0,22,2)]
print('listeE')
print(listeE)

#Man kan også anvende den indbyggede objekt list der omsætter en sekvens til en liste
# L = list(sequence)
listeF=list(range(1,30,3))
print('listeF')
print(listeF)

#Længden af en liste
print(len(listeE))

#Trække et element ud med nummer
print(listeE[5])

#Lave en ny liste
pluk = listeE[3:7] #Tager element nr 3-7. Husk en liste starter med 0 så nr 3 er fjerde element
print('pluk')
print(pluk)

#springe elementer over
pluk1 = listeE[3:7:2] #Tager hverandet element fra nr 3-7. 
print(pluk1)

# Tager hverandet element af hele listen
pluk2=listeE[::2]
print(pluk2)

# Tager resten af listen fra et punkt
pluk3=listeE[4:]
print(pluk3)

# Tager starten af listen før et punkt
pluk4=listeE[:4]
print(pluk4)

# Tager sidste element
pluk5=listeE[len(listeE)-1]
print(pluk5)
#Dette gøres lettere med -1 hvor længden er underforstået
pluk6=listeE[-1]
print(pluk6)
#På samme måde med alle negative elementnumre
pluk7=listeE[-5] #her 5'te sidste element
print('pluk7')
print(pluk7)

#Gennemgå liste og anvende (f.eks. printe) elementerne
for element in listeE:
    print(element,end=" ")

print('')

#Hvis både element nr og element skal anvendes skal objektfunktionen enumerate anvendes
for nr,element in enumerate(listeE):
    print(nr,' ',element)

# Man kan også anvende en iterator
mintaeller = iter(listeE)
element1 = next(mintaeller) # fetch first value
element2 = next(mintaeller) # fetch second value
print(element1,' ',element2)

# Matematiske funktioner på lister med tal
#sum af liste
print(sum(listeE))
#sum af liste med startsum
print(sum(listeE, 100))
#gennemsnit af liste
print(float(sum(listeE)) / len(listeE))

#Alternativ opsummering med for løkke
MinSum=0
for element in listeE:
    MinSum+=element
print(MinSum)

#Eksempel Her vi vi kun summere tal og undlade tekstelementer
# Funktion. Check om det er et tal

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print(is_number(34))
print(is_number('er'))

MinSum=0
for element in listeB:
    if is_number(element):MinSum+=element
print(MinSum)

#Hvis listen kun indeholder strings kan hele listen lægges i en string med en separator
s=';'
print(s.join(listeC))
#eller uden separator
print(''.join(listeC))

#Modificere liste
#Element til sidst-append
print (listeB)
listeB.append(27)
print (listeB)

listeG=['abe']
print(listeG)
listeG.extend(listeB[:])
print(listeG)
listeG.extend(listeC[:])
print(listeG)
print(len(listeG))

#Indstter element og skubber øvrige
listeG.insert(8, 'abekat')
print(listeG)
print(len(listeG))

#Indsætte enkelt element fra anden liste
listeG.insert(4, listeB[5])
print(listeG)

#pas på når du sætter to lister lig hinanden så peges der på samme punkt og begge ændres
L = []
M = L
# modify both lists
L.append('Knud')
print(L)
print(M)

#istedet sættes den nye liste lig den gamles elementer. Her forbliver M tom
L = []
M = L[:]
# modify one list
L.append('Knud')
print(L)
print(M)

# Lægge lister sammen
NY=[]
NY=listeG+listeE    #liste
print(NY)

Ny1=[]
NY1=listeG,listeE   #matrix
print(NY1)

#Slette fra lister
#Fjerne led nummer 5
del NY[5]
print("nummer 5 er fjernet ",NY)
del NY[6:8]
print("numer 6+7 er fjernet ",NY)
item = NY.pop()     # fjerner sidste led og sender det tilbage
print("sidste fjernet og printet ",NY)
print(item)
item = NY.pop(0)     # fjerner første led og sender det tilbage
print("første fjernet og printet ",NY)
print(item)
item = NY.pop(8) #fjerner en nummereret led og sender det tilbage
print("numer 8 er fjernet og printet ",NY)
print(item)

NY.remove("Dig")
print("'Dig' er fjernet ",NY)

NY.remove(196)
print("196 er fjernet ",NY)

# Med reversere kan listen vendes. En hurtig måde at indsætte i start af liste
NY.reverse()
# append/insert/pop/delete at far end
NY.append("JegStarter")
NY.reverse()
print(NY)

#NB NB Bemærk at det ikke virket, da tælleren ændrer sig og vi fjerner element.
#Derfor springes element over som ikke jernes
for nr,element in enumerate(NY):
    if is_number(element):
        del NY[nr]
        print(nr)
print(NY)

for element in NY:
    if is_number(element):
        NY.remove(element)
        print(element)
print(NY)

NY=listeG+listeE
print(NY)

#Problemet løses ved at opsamle den nye liste separat
NYud=[]
for element in NY:
    if not(is_number(element)):
        NYud.append(element)
print("samle op i ny liste ",NYud)

# Erstatte et led med resultatet af en funktion
# For eks. Hvis det er et tal så lægge vi 50% ovenpå

def tillaeg(ind):
    if is_number(ind): ud=1.5*ind
    else: ud=ind
    return ud

print(tillaeg(120))
print(tillaeg("finn"))

#Her tillægges 50% på hver tal-led
NY=listeG+listeE
print(NY)
for index, element in enumerate(NY):
        NY[index] = tillaeg(element)
print(NY)

#Dette kan også gøres med ny funktion
NY=listeG+listeE
print(NY)
NYud=[]
for element in NY:
    NYud.append(tillaeg(element))
print("Ny liste ",NYud)   

#Mere effektivt kan dette gøres med list comprehension
NY=listeG+listeE
print(NY)
NYud=[]
NYud=[tillaeg(element) for element in NY]
print("liste comprehension ",NYud)

#Mere effektivt kan dette gøres med map. Bemærk at map object konverteres til liste
NY=listeG+listeE
print(NY)
NYud=[]
NYud=list(map(tillaeg,NY))
print("mapping ",NYud)

#Flytte element til slut på liste

NYud.remove(" og")
NYud.append(" og")
print(NYud)

#Undersøge om et element er i listen

if "Mig " in NYud:
    print("yes 'Mig' er i listen")
else: print("bedre held næste gang")

# Finde første nr der svarer til et element
test="Mig "
if test in NYud:
    print("yes test er nr: ",NYud.index(test))
else: print("bedre held næste gang")


#Tælle antal forekomster af et element
test="Mig "
if test in NYud:
    print("yes test forekommer antal gange: ",NYud.count(test))
else: print("bedre held næste gang. Du fandt så mange:", NYud.count(test))

# min og max. kan kun anvendes på tallister.
print(min(listeF))
print(max(listeF))
