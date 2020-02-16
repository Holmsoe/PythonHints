
import time
from math import sqrt,log

def primtal(n):
    # n er max der testes
    # itest er det tal der aktuelt testes
    # memo er liste over primtal op til itest
    memo = [2]

    for itest in range(3,n):
        j=2
        OK=True
        while j<=sqrt(itest) and OK:
            if itest%j==0: OK=False
            j=j+1
        if OK: memo.append(itest)
    
    return memo

start = time.time()
maxtal=100000
Alle=primtal(maxtal)
Antal=len(Alle)
Sidste=Alle[Antal-1]
print("max=",maxtal,"antal=",Antal,"Sidste=",Sidste)
#print("teoretisk antal ",int(maxtal/log(maxtal)))

end = time.time()
print("tid ",end - start)

#Anvend allerede beregnede primtal

def primtalA(n):
    # n er max der testes
    # itest er det tal der aktuelt testes
    # memo er liste over primtal op til itest
    memo = [2]

    for itest in range(3,n):
        OK=True
        lang=len(memo)-1
        j=0
        while OK and j<=lang:
            if itest%memo[j]==0: OK=False
            j=j+1
        if OK: memo.append(itest)
    
    return memo

start = time.time()
maxtal=100000
Alle=primtalA(maxtal)
Antal=len(Alle)
Sidste=Alle[Antal-1]
print("max=",maxtal,"antal=",Antal,"Sidste=",Sidste)
#print("teoretisk antal ",int(maxtal/log(maxtal)))

end = time.time()
print("tid ",end - start)

# rekursion
#======================



def isprime(itest,n):
    if itest == 1:
        return True
    else:
        #print(itest,n)
        if n%(itest)==0:
            return False
        else:
            return isprime(itest-1,n)


 

start = time.time()  
maxprime=100000
gemmeprimtal=[]
#Vi starter test ved sqrt(n) for at undgå dobbelt
for i in range(2,maxprime):
    if isprime(int(sqrt(i)),i): gemmeprimtal.append(i)
print("Sidste ",gemmeprimtal[-1],"Antal ",len(gemmeprimtal))

end = time.time()
print("tid ",end - start)
