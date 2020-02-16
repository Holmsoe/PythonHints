minrange=[5,11]

# * henter en anden range
print('list anvendt som range')
for i in range(*minrange):
    print (i,i*i,end=' ')
print('')

# Tuples med og uden parenteser
tuple1=(1,'Finn',2,'Vesna',3,'Øf','ekstra')
tuple2=111,'Ugh',212,'Bingo',313,'Opa'
tuple1a=999,'lille',1111,'liste'

print(tuple1[5])

print('')
tuple3=tuple1,tuple2,tuple1a # med , lægges de i matrix
print('kombinere tuples med , (komma)')
print(tuple3)
print('tuple3[1][1]')
print(tuple3[1][1])
print('')

tuple4=tuple1+tuple2+tuple1a # med+ lægges de i linie
print('kombinere tuples med + ')
print(tuple4)

#Printe 2D tuple med koordinater og indhold
antalLinier=len(tuple3)
for i in range(0,antalLinier):
    for j in range(0,len(tuple3[i])):
        print(i,j,tuple3[i][j])
print('')
tuple5=[]
for i in range(0,len(tuple4)):
    tuple5.append(str(tuple4[i])) #tuple4 lægges over i tuple5 som string
print('tuple5')
print(tuple5)
print('')
#Dette kan gøres efter konvertering til string
tuple6=sorted(tuple5) # sortering kan kun foregår på ens datatyper
print('sortering af tuple')
print(tuple6)
print('')

# Her sorteres en matrix efter kolonne nr 3 som er 4. kolonne. Dette styres i item[3]

def getKey(item):
    return item[3]

#sortering med key. getkey tager hver linie som argument og returnerer 3 søjle
tuple7=sorted(tuple3,key=getKey)
print('sortering af 2D tuple med key')
for line in tuple7:
    print(line)
print('')
print('filter på tuple')
for i in range(0,len(tuple6)):
    if tuple6[i]<'Danmark': print(i,tuple6[i])
print('')
# Lave en liste med filter på tuple
fliste1 = list(filter(lambda x: x < 'Danmark', tuple6))
print('liste med filterresultat fra 1D tuple')
print(fliste1)
print('')
# Filter en matrix hvor 3 søjle er mindre end 200
fliste2 = list(filter(lambda x: x[2] > 200, tuple3))
print('liste med filterresultat fra 2D tuple')
print(fliste2)


