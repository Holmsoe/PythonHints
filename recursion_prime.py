
import time
from math import sqrt

start = time.time()

def primtal(n):
    memo = {1:2}
    counter=1
    for itest in range(3,n):
        primeOK=True
        #for j in range(1,1+int(sqrt(len(memo)))):
        j=1
        while memo[j]<sqrt(itest) and j<=len(memo):    
            if itest%memo[j]==0:
                print (j,memo[j])
                primeOK=False
                #break
            j=j+1
            print(j)
            
        if primeOK:
            counter=counter+1
            memo[counter]=itest   

    
    return memo
maxPrimtal=10
AllePrimtal=primtal(maxPrimtal)
AntalPrimtal=len(AllePrimtal)
SidstePrimtal=AllePrimtal[AntalPrimtal]
print("max=",maxPrimtal,"Antal=",AntalPrimtal,"Sidste=",SidstePrimtal)

end = time.time()
print("tid ",end - start)
print(AllePrimtal)
