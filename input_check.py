def indlaes(spoergetekst,gentag=4,tjekke='Svar ja eller nej, tak!'):
    while True:
        inputtekst=input(spoergetekst)
        if inputtekst in('ja','j','yes','yep','y'):
            return True
        if inputtekst in('nej','n','no','n','nope'):
            return False
        gentag=gentag-1
        if gentag<0:
            return False
            break
        print(tjekke)
        
        
if indlaes('Videre????'):
    print('Ok vi fortsætter')
else:
    print('Ok vi slutter')

if indlaes('Snustobak',1,'Kom nu spasser'):
    print('Ok vi fortsætter')
else:
    print('Ok vi slutter')
