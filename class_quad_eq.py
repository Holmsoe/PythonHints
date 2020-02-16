
class andengrad:
    a=0
    b=0
    c=0
    def skriv(self):        #self skal anvendes selvom der ikke er argumenter
        print("100*")
        
    def rod(self,a,b,c):   #en metode med argumenter 
        print(a,b,c)
        d=b**2-4*a*c
        r1=(-b+d**0.5)/(2*a)
        r2=(-b-d**0.5)/(2*a)
        return(r1,r2)
    
    def rod1(self,a,b,c):
        d=b**2-4*a*c
        r1=(-b+d**0.5)/(2*a)
        return r1
    
    def rod2(self,a,b,c):
        d=b**2-4*a*c
        r2=(-b-d**0.5)/(2*a)
        return r2
    def toppunkt(self,a,b,c):
        d=b**2-4*a*c
        xt=-b/(2*a)
        yt=-d/(4*a)
        return (xt,yt)

MinLigning=andengrad() #initialiserer en instance af klassen

# Kald af metode uden variabel 
MinLigning.skriv()

# Kald af variabel i klasse
print(MinLigning.a)                     #Dette er normal skrivemåde. Format: Instance.variabel
#Alternativ format
print("her er den")
andengrad.skriv(MinLigning)    #Dette er formaliseret der forklarer self kodeordet. Format: Class.Method(Instance) 
                                        #Modsvarer  struktur i klasse: Class->Method->Instance=self
#kald med parametre
r1=0
r2=0
MinLigning.rod(3,-3,-6)
#Bemærk at variabel ikke ændres ved kald med parametre
print(MinLigning.a)

#Her ændres parameter
MinLigning.a=4
print(MinLigning.a)

#Her printes a,b,c (internt i metoden) og herefter de to variable der returneres fra metode
print(MinLigning.rod(3,-3,-6))
#Først af de returnerede uddrages
print(MinLigning.rod(3,-3,-6)[0])
#Anden af de returnerede uddrages
print(MinLigning.rod(3,-3,-6)[1])

print("Nye rødder")
print(MinLigning.rod1(3,-3,-6))
print(MinLigning.rod2(3,-3,-6))

#Toppunkt
print("Toppunkt:  X=" +str(MinLigning.toppunkt(3,-3,-6)[0]) +", Y="+str(MinLigning.toppunkt(3,-3,-6)[1]))
