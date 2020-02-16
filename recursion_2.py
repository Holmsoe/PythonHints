
import time
from math import sqrt

start = time.time()

def sumn(n):
    if n == 1:
        return 1
    else:
        return n + sumn(n-1)
#print(sumn(5))


minliste=[i for i in range(1,60)if i%7==0 or i%5==00]
print(minliste)

def sumliste(mylist,n):
    indreliste=mylist
    if n==0:
        return indreliste[0]
    else:
        return indreliste[n]+sumliste(indreliste,n-1)
    
sidste=len(minliste)-1
print(sumliste(minliste,sidste))


def sumlisteA(mylist):
    if not mylist:  #checker om liste er tom
        return 0
    else:
        return mylist[0]+sumlisteA(mylist[1:]) # bemærk slicing teknikken for resten af listen
print(sumlisteA(minliste))

def isprime(itest,n):
    if itest == 1:
        return True
    else:
        #print(itest,n)
        if n%(itest)==0:
            return False
        else:
            return isprime(itest-1,n)

#Vi starter test ved sqrt(n) for at undgå dobbelt
pTjek=61
print(isprime(int(sqrt(pTjek)),pTjek))  
    
maxprime=100
for i in range(2,maxprime):
    if isprime(int(sqrt(i)),i):
        print(i," ",end="")
    
