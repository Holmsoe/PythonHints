
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


#Funktion der læser csv fil og omdanner til liste
#############################################
def laesefil(filnavn):
    with open(filnavn,'r') as Minfil: 
        minmatrix=[]
        for line in list(Minfil): minmatrix.append(line.split(";"))
    return minmatrix
#############################################


#Funktion der sorterer efter en kolonne, printer tabel og afpasser kolonnebredde
#############################################

def printmatrix(minmatrix,sorterkolonne):

    # Finde kolonnebredde
    colbredde=[]                    #Gemme kolonnebredder
    transmatrix=bytte(minmatrix)    #transponere matrix og finde kolonnebredde ved at gennemgå række i den transponerede    
    for line in transmatrix:
        maxtext=0
        for element in line:
            if len(element)>maxtext: maxtext=len(element)
        colbredde.append(maxtext)

    #Konvertere tal fra string til tal    
    r=len(minmatrix)
    s=len(minmatrix[0])
    for i in range(r):
        for j in range(s):
            try:
                minmatrix[i][j]=int(minmatrix[i][j])
            except ValueError: 
                pass

    #Fjerne overskrift fra tabel
    overskrift=[]
    overskrift.append(minmatrix[0])
    minmatrix.pop(0) #fjerne første række

    #Sortere tabel
    nymatrix=sorted(minmatrix, key=lambda kolonne: kolonne[sorterkolonne],reverse=False)
        
    #Printe tabel
    #Overskrift
    for line in overskrift:
        print("")
        for elementnr,element in enumerate(line):
            print('{:{bredde}}'.format(str(element),bredde=colbredde[elementnr]+2),end="")
    #Tabel
    for line in nymatrix:
        print("")
        for elementnr,element in enumerate(line):
            print('{:{bredde}}'.format(str(element),bredde=colbredde[elementnr]+2),end="")

#############################################       

minmatrix=laesefil('materialer.txt')
printmatrix(minmatrix,1)



