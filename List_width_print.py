
minliste=[["Abe","01-05-2018",345.45,1223],["Skorstensabekat","12-01-2018",57.5,1300],["Cykel","21-02-2018",135,1400],["Glasbur","19-03-2018",20.5,1350],["Trillebør","27-03-2018",530.60,1160],["Baldakin","07-02-2018",222.90,1210]]

def BeregnKolonnebredde(minmatrix):
    OKtabel=True
    Nkolonner=len(minmatrix[0])
    kolonnebredde=[0 for i in range(Nkolonner)]
    for line in minmatrix:
        if len(line)==Nkolonner:
            for nr,item in enumerate(line):
                if len(str(item))>kolonnebredde[nr]:
                    kolonnebredde[nr]=len(str(item))
        else:
            OKtabel=False
            print("stop tabellen har ikke samme antal kolonner")
    return kolonnebredde

def LinieTilTekst(liste,kolonnebredde):
    linietekst=""
    for nr,item in enumerate(liste):
        linietekst+="{tekst:{bredde}s} ".format(bredde=kolonnebredde[nr],tekst=str(item))
    return linietekst        

kolonnebredde=BeregnKolonnebredde(minliste)

for line in minliste:
    print(LinieTilTekst(line,kolonnebredde))
    

