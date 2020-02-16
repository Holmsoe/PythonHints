#Print tal 1-5 i samme linie
for i in range(0,5):
    print (i,end=" ")

print('')

#Print 5 lige tal i samme linie    
for i in range(0,10,2):
    print (i,end=" ")

print('')

#Printe fibonaccital med ny linie efterhånden som de beregnes
def fib(n):
    a,b=0,1
    while a<n:
        print(a)
        a,b=b,a+b

#Beregne fibonaccital, gemme i liste og returnere liste fra funktion
def fib1(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result
    
#Her printes i funktionen
fib(100)

#Her returneres liste som herefter printes som liste
print (fib1(100))

#Her printes elementer fra liste
for i in fib1(100):
    print(i,end=" ")

print('')
minlist=[1,2,3,5,7,11]

for i in minlist:
    print(i,end=" ")

#Beregn primtal og gem i liste
def prime(n):
    primelist=[2]
    a=3
    while a<n:
        test=0
        for x in primelist: 
            if a % x == 0:
                test=1
                break
        if test==0:
            primelist.append(a)
        a=a+1
    return primelist

print ('')

#Skriv liste med primtal
print(prime(100))

#Skriv antal primtal
print(len(prime(100)))

