
import tkinter as tk
from tkinter import font

mitvindue=tk.Tk()
mitvindue.configure(background='gray80')

FarveOversigt={}

with open('SAPfarveliste.txt','r') as Minfil:
    for linie in Minfil:
        linieliste=[]
        try:
            # 2 cifre i nummer
            nr=int(linie[0:2])
            dictvalue=linie[4:-3]
            for item in dictvalue.split(","): linieliste.append(item)
            FarveOversigt[nr]=linieliste       
        except:
            nr=int(linie[0:1])
            dictvalue=linie[3:-3]
            for item in dictvalue.split(","): linieliste.append(item)
            FarveOversigt[nr]=linieliste

minfarve=[]
minfarvenavn=[]
minramme=[]
mintekst=[]

#minFont=font.Font(family="Monaco", size=10) #samme bredde font = monospaced
minFont=font.Font(family="Courier", size=10) #samme bredde

for farvenr in FarveOversigt:
    nyfarve="#%02x%02x%02x" % (int(FarveOversigt[farvenr][0]),int(FarveOversigt[farvenr][1]),int(FarveOversigt[farvenr][2]))
    rgbfarve=[FarveOversigt[farvenr][0],FarveOversigt[farvenr][1],FarveOversigt[farvenr][2]]
    nyfarvenavn=FarveOversigt[farvenr][3]
    udtekst='{:15}{:5}{:5}{:5}'.format(nyfarvenavn,rgbfarve[0],rgbfarve[1],rgbfarve[2])
    minfarve.append(nyfarve)
    minfarvenavn.append(nyfarvenavn)
    minramme.append(tk.Frame(mitvindue, bg =nyfarve,width=60,height=10))
    mintekst.append(tk.Label(mitvindue,text=udtekst,bg='gray80',font=minFont,padx=20))

colnr=0
rowminus=0
linierperkolonne=20
dummytekst=tk.Label(mitvindue,text="",bg='gray80',pady=10)
dummytekst.grid(row=0,column=0)
for i in range(len(FarveOversigt)):
    if i%linierperkolonne==0 and i>0:
        colnr+=2
        rowminus+=linierperkolonne
    mintekst[i].grid(row=i+1-rowminus,column=colnr)
    minramme[i].grid(row=i+1-rowminus, column=colnr+1)


mitvindue.geometry('1200x550')
mitvindue.mainloop()



