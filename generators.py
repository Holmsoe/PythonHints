nmax=20
nmin=10
#Bemærk, at generatorer leverer en værdi ad gangen og husker hvor langt den er kommet.
#Derfor kan den heller ikke kaldes flere gange men bliver opbrugt.

#iAnden er defineret ud fra en liste og er en iterator
iAnden = iter([i*i for i in range(nmin,nmax)])

#square is a generator
square = (i*i for i in range(nmin,nmax))

#square defined in function herefter sættes interator hvor next() kan anvendes
def squares(nmin, nmax):
    for i in range(nmin, nmax):
        yield i * i
        
minsquare=squares(nmin,nmax)    #Her defineres generator
minsquare1=squares(1,10)        #Der kan defineres mange generator ud fra samme funktion.
                                #Herved kan definitionen i funktionen genbruges.

#add the squares. Der laves ikke en liste men square giver en værdi ad gangen
#Bemærk, at det er summen af i*i og ikke af i der beregnes. Værdien hentes fra Generator
total = 0
for q in square:
    total += q
print('')
print('generator square')
print(total)

total1=0
for q in minsquare:
    total1 += q
print('')
print('generator minsquare')
print(total1)    

total2=0
#for s in minsquare1: print(s,end=" ")
#HVis denne sætning indsættes er iterator opbrugt til sum
for q in minsquare1:
    total2 += q
print('')
print('generator minsquare1')
print(total2)    

#Bemærk, at iterator minsquare og minsquare1 nu er opbrugt og ikke kan kaldes mere med next

#
print("")
print(next(iAnden))
print(next(iAnden))

#Fibonacci
def Fibonacci(nmax):
    a=0
    b=1
    while b < nmax:
        yield b
        atemp=a
        a=b
        b=atemp+b
        
minFibo=Fibonacci(100)
minFibo1=Fibonacci(100)
minFibo2=Fibonacci(100)

for q in minFibo:   #Her hentes alle elementer i Fibonacci et efter et
    print(q)

sumFib=sum(minFibo1)    #Bemærk denne konstruktion. Alle elementerne i minFibo1 kendes og kan direkte summeres
print(sumFib)

for i in range(5):      #Herprintes de 5 første elementer af minFibo2
    print(next(minFibo2))

print("Her kommer den næste")
print(next(minFibo2))


