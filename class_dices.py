
import random
import math

def binom(n,k,p):
    ud=math.factorial(n)/math.factorial(k)/math.factorial(n-k)*math.pow(p,k)*math.pow(1-p,n-k)  
    return ud

def Knk(n,k):
    ud=math.factorial(n)/math.factorial(k)/math.factorial(n-k)
    return ud

def sumsandsynlighed(aktuelsum,antalterninger,sider):
    # se http://mathworld.wolfram.com/Dice.html  
    kmax=math.floor((aktuelsum-antalterninger)/sider)
    sumP=1/math.pow(sider,antalterninger)*sum(math.pow(-1,k)*Knk(antalterninger,k)*Knk(aktuelsum-sider*k-1,antalterninger-1) for k in range(kmax+1))
    return sumP

class Terninger (object):
    
    def __init__ (self, sider=6,antal=2,slag=10):
        self.sider =sider
        self.antal=antal
        self.slag=slag

    def slaa(self):
        slagliste=[[random.randint(1,self.sider) for s in range(self.antal)] for n in range(self.slag)]
        sumliste=[sum(r) for r in slagliste]
        maxslag=self.sider*self.antal
        minslag=self.antal
        taeller=[sumliste.count(i) for i in range(minslag,maxslag+1)]
        sandsynlighed=[sumsandsynlighed(aktuelsum,self.antal,self.sider) for aktuelsum in range(minslag,maxslag+1)]
        #print(slagliste)
        #print(sumliste)
        #print(taeller)
        print("Antal terninger: ",'{:3d}'.format(self.antal))
        print("Antal sider:     ",'{:3d}'.format(self.sider))
        print("Antal slag:      ",'{:3d}'.format(self.slag))
        print("")
        print("Sum Antal P-aktuel Sansynlighed")
        for i in range(minslag,maxslag+1):      
            print('{:3d}  {:3d}    {:05.3f}    {:05.3f}'.format(i,taeller[i-minslag],taeller[i-minslag]/self.slag,sandsynlighed[i-minslag]))

            
mitspil=Terninger()
stortspil=Terninger(6,4,216*6)

#mitspil.slaa()
stortspil.slaa()


#print(sumsandsynlighed(3,3,6))
