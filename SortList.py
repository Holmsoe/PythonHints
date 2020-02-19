
li = [[2,6],[9,3],[5,4],[6,5],[1,8]]
lisort=sorted(li,key=lambda linie:linie[0],reverse=True) #New list. Efter størrelse i kolonne
lisort1=sorted(li,key=lambda linie:linie[0]%2==0)
#New list. Her kommer først alle ulige i første kolonne i oprindelig rækkefølge og herefter lige.
#Ulige først fordi False giver 0-værdi.
print(li)
print(lisort)
print(lisort1)
li.sort(key=lambda linie:linie[0],reverse=True)     #In place
print(li)
'''
My sort method obviously says, "Please sort this list".
The key argument makes that a little more specific by saying,
for each element (linie) in mylist, return index 0 of that element,
then sort all of the elements of the original list 'li' by
the sorted order of the list calculated by the lambda function.
 
'''

li1=[row for row in li if row[0]==5]    #alle hvor første kolonne er 5
print(li1)
li2=[row for row in li if row[0]%2==0]  #Alle hvor første kolonne er lige
print(li2)

with open("udgifter.txt") as minfil:
    lines=minfil.readlines()


maaneder={1:"Januar",2:"Februar",3:"Marts",4:"April",5:"Maj",6:"Juni",7:"Juli",8:"August",9:"September",10:"Oktober",11:"Novenber",12:"December"}
print(maaneder[3])
for line in lines:
    maaned=int(line.split(";")[1][3:5])
    print(maaneder[maaned])
    
li3=[line for line in lines if int(line.split(";")[1][3:5])==5]
print(li3)

#Indlæste udgifter sorteres efter maaned faktura
li4=sorted(lines,key=lambda line: int(line.split(";")[1][3:5]))
print(li4)
for line in li4:
    maaned=int(line.split(";")[1][3:5])
    print(maaned," ",maaneder[maaned])
    
#Den sorterede liste anvendes til filter på marts til maj
li5=[line for line in li4 if int(line.split(";")[1][3:5])>=3 and int(line.split(";")[1][3:5])<=5]
print(li5)
