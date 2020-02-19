
minliste=[["Finn","01-05-2018","107.5","2660"],["Vesna","01-02-2018","1250.5","2670"],["Gurli","01-07-2018","222.5","2680"],["Bent","01-10-2018","23.5","2660"],["Pia","01-07-2018","744.5","2670"],["Bamse","01-09-2018","378.5","2660"]]
ekstra=["Houdini","17-09-2018","1235.70","2680"]
liste2=[["KarlBørge","27-02-2018","36.9","2670"],["BillyBob","03-12-2018","650.50","2660"]]
bogstaver=["q","g","c","5","e","y","v","c","3","a","z","o","1","b","m","r"]

kopiliste1=minliste                       # de to lister er identiske - også efter ændringer af den ene
kopiliste2=minliste.copy()                # en ny uafhængig liste

print("antal linier =",len(minliste[:]))     #antal linier.len(minliste) er også OK
print("elementer i linie =",len(minliste[0])) #længde af hver linie
print(minliste[0])

#Append. Indsætte element i sluting af liste
minliste.append(ekstra)
print("antal linier =",len(minliste))     #antal linier
print(minliste[6])
print("antal linier-en kopieretliste,ændres når liste ændres =",len(kopiliste1)) # Bemærk en kopieret liste er identisk med den oprindelige - også efter ændringer
print("antal linier-kopieret med .copy(),ændres ikke =",len(kopiliste2))



#Count
x=minliste[0].count("2660") #tæller i en linie
print("antal 2660 i en linie = ",x)

x=0
for linie in minliste:      #tælle  i en matrix
  x+=linie.count("2660")
print("antal 2660 i matrix= ",x)

#Extend. Lægge to lister sammen.
minliste.extend(liste2)
print("antal linier af extended liste =",len(minliste))     #antal linier

# Index. Finder placering af første element (ikke deltekst-hele elementet)
i=minliste[0].index("2660")
print("Vi finder i position ",i)


#insert. Indsætte et element på en position.
print("liste2 før indsæt=",liste2)
liste2.insert(1,ekstra) #Hvis pos er større end antale elementer er det append.
print("liste2 efter indsæt=",liste2)

#Pop. Fjerner element på basis af position
liste2.pop(1)
print("liste2 efter pop=",liste2)

#remove. Fjerner element på basis af value
print("ekstra før remove=",ekstra)
ekstra.remove("2680")
print("ekstra efter remove=",ekstra)

#reverse. Vender rækkefølge rundt.
print("liste2 før reverse=",liste2)
liste2.reverse()
print("liste2 efter reverse=",liste2)

#Sorterer en liste alfabetisk. Husk oprindelig liste overskrives
print(bogstaver)
bogstaver.sort()
print(bogstaver)

#Clear. Fjerne elementer fra liste
minliste.clear()
print("antal linier efter clear =",len(minliste))     #antal linier

