
'''
================= START PÃ
 KLASSE   ================================
'''
class ListeKlasse():
    def __init__(self,DataListe):

        self.MinMatrix=DataListe
        self.Nkolonner=len(self.MinMatrix[0])
        self.Nlinier=len(self.MinMatrix)
        self.kvartal={1:1,2:1,3:1,4:2,5:2,6:2,7:3,8:3,9:3,10:4,11:4,12:4}
        
         
#======================================
#============= Filter med en sandhedsfunktion og list comprehension
 
    def Ogfilterlinie(self,mitfilter,linie):
        test=True
        for item in mitfilter:
            minkey=int(item) #kolonnenummer
            minvalue=mitfilter[item] #Vaerdi der skal vaere opfyldt i kolonne
            if linie[minkey]!=minvalue: test=False
        return test
   

    def OgFilter(self,mitfilter):
        nyliste=[linie for linie in self.MinMatrix if self.Ogfilterlinie(mitfilter,linie)]
        '''
        her indsaettes sletning af de berigede kolonner inden ny liste returneres
        '''
        return nyliste
    
#============== Slet linie
    def SletLinie(self,linienr):
        del self.MinMatrix[linienr]

        
#============== Ret linie
    def RetLinie(self,linienr,nylinie):
        self.MinMatrix[linienr]=nylinie   

#============== Udskriv matrix med tilpasset kolonneredde   
    def UdskrivMatrix(self):
        PrintBredde=self.KolonneBredde(25)  #Max kolonnebredde er 25
        for line in self.MinMatrix:
            udtext=""
            for col,item in enumerate(line):
                colbredde=PrintBredde[col]
                udtext+='{a:{b}.{b}} '.format(b=colbredde,a=str(item))
            print(udtext)

            
    def KolonneBredde(self,MaxKolonneBredde):
        antalkolonner=len(self.MinMatrix[0])
        #print(antalkolonner)
        bredde=[0 for i in range(antalkolonner)]     
        for line in self.MinMatrix:
            for col,item in enumerate(line):
                #print("col=",col,item)
                #print(line)
                if len(str(item))>bredde[col]:
                    if len(str(item))<=MaxKolonneBredde:
                        bredde[col]=len(str(item))+2
                    else:
                        bredde[col]=MaxKolonneBredde                              
        return bredde

'''
================= SLUT PAA KLASSE   ================================
'''
def cleanCSV(line):
    temp=line.rstrip()
    nylinie=temp.split(";")
    return nylinie

with open("udgifter.txt",'r') as Minfil:
        NyListe=[cleanCSV(line) for line in Minfil]

MinListe1=ListeKlasse(NyListe)


#Paa basis af første liste laves en filtreret liste
mitfilter={5:"1",6:"0"} #Filter
filterliste=MinListe1.OgFilter(mitfilter)
MinFilterListe=ListeKlasse(filterliste)
MinFilterListe.UdskrivMatrix()
print("")

#Slet linie 0 i oprindelig matrix
nr=0
MinListe1.SletLinie(nr)

#Indsaet ny linie i oprindelig matrix
#nylinie=['Hulabula','01-09-2018','01-10-2018','235.65','25','1','1','0','1','2770 Rejseudgifter']
#MinListe1.RetLinie(0,nylinie)

print("foerste linie er slettet")
MinListe1.UdskrivMatrix()

