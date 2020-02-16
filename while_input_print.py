#=========================================
#While løkke
#Lave string med tal under 10 og udskrive
a=1
b=''
while a<10:
    b=b+ str(a)
    a=a+1 
print(b)
#=========================================

#Printe uden linieskift

#Flere erklæringer i samme linie. unpack
c,d=3,4
c,d,e = d,c+d,c*d
print(c,end=" ")
print(d,end=" ")
print(e,end=" ")
#print(b)

#=========================================

#Input og test af inputdata
x=input("Please enter an integer: ")
print(x)
y=int(x)
z=y%2

if y<0:
    print('tallet er mindre end 0 din Ork')
elif y % 2 == 0:
    print('Du har givet et lige tal')
elif y % 3 == 0:
    print('3 går op i tallet og tallet er ulige')
else:
    print('det er et fjollet tal')

print('slut på if')


#Printe fra liste 
tekst=['Hej', 'med', 'dig', 'din','abekat']
for w in tekst:
    print(w,end=' ')

for i in range(10):
    print(i,end=' ')

for i in range(len(tekst)):
    print(tekst[i],end=' ')
