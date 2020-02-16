
import datetime

def datoeks(aar,maaned,dag):
    dato=datetime.date(aar,maaned,dag)
    print("yy-mm-dd    ",dato)
    print("maaned tekst",dato.strftime("%B"))
    print("mm/dd/yy    ",dato.strftime("%x"))
    print("dd          ",dato.strftime("%d"))
    print("mm          ",dato.strftime("%m"))
    print("yyyy        ",dato.strftime("%Y"))
    
def datotiltekst(dato):
    mindato=dato.strftime("%d")+"-"+dato.strftime("%m")+"-"+dato.strftime("%Y")
    print(mindato)
    
def teksttildato(datotekst):
    dato=datetime.date(int(datotekst[6:10]),int(datotekst[3:5]),int(datotekst[0:2]))
    print(dato)
    
def tjekdato(datotekst):
    try:
        dato=datetime.date(int(datotekst[6:10]),int(datotekst[3:5]),int(datotekst[0:2]))
        print("OK")
    except ValueError as fejl:
        print("fejl:",fejl)
    

    
datoeks(2018,9,20)
dato=datetime.datetime(2018,9,20)
datotiltekst(dato)
teksttildato("30-09-2018")
tjekdato("40-09-2018")

