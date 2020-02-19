import tkinter as tk
import random
import csv
window=tk.Tk()

def vaelg_verbum():
    with open('verber-csv.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        mine_verber = list(spamreader)
    liste_verber=mine_verber[0][0].split(";")
    
    verbum=random.choice(liste_verber)
    return verbum

def vaelg_substantiv():
    with open('substantiver-csv.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        mine_substantiver = list(spamreader)
    liste_substantiver=mine_substantiver[0][0].split(";")
        
    substantiv=random.choice(liste_substantiver)
    return substantiv

def Min_Knap():
    navn=Input_navn.get()
    verbum=vaelg_verbum()
    substantiv=vaelg_substantiv()
    tekst=navn + " " + str(verbum) + " " + str(substantiv)
    mit_vindue.delete(0,tk.END)
    mit_vindue.insert(0,tekst)

navnLabel=tk.Label(window,text="Navn:")
Input_navn=tk.Entry(window)
Knap=tk.Button(window,text="Lav tekst",command=Min_Knap)
mit_vindue=tk.Entry(window)

navnLabel.pack()
Input_navn.pack()
Knap.pack()
mit_vindue.pack()
window.mainloop()

print(tekst)
