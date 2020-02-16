class minklasse:

    def __init__(self, a=7,b=3,c=4):    #Dette er mekanisme for globale variable der så adresseres som feks self.a
        self.a=a
        self.b=b    #de globale variable
        self.c=c
       
    def skriv(self,a,b,c ):
        print("Her skrives de 'globale' variable som arves fra initialisering:", self.a,self.b,self.c)
        print("Her skrives de aktuelle inputvariable:", a,b,c)
        
    def __str__(self):
        return "parametre {}, {}, {}".format(self.a, self.b,self.c)
        
        
#def_init sikrer, at variable sættes ved definition af nyt objekt.

FinnClass=minklasse() #Her defineres et objekt uden parameter. Så anvendes initialiseringsværdi fra def_init
print("a fra initialisering:", FinnClass.a)

FinnClass.skriv(4,5,6)

FinnNy=minklasse(5)  #Her defineres et objekt med parameter
print("a fra kaldet. En parameter er nok selvom der er 3 variable der initialiseres:",FinnNy.a)


MinNy=minklasse(c=34)
print("Her tillægges ny værdi for c:", MinNy.a,MinNy.b,MinNy.c)

MinNy1=minklasse(3,7,11)
MinNy1=minklasse()
print("Hvis ikke parameter defineres i kaldet anvendes initialiseringen uanset og der er et tidligere kald",MinNy1.a,MinNy1.b,MinNy1.c)

#Denne anvender __str__ for at printe
print(FinnClass)