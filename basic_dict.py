dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print(dict)
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#key and value can be all datatypes
dict2={1: "Kaj",2:"Jens"}
print(dict2)
print(dict2[1])

#copy dict and add new member
dict3=dict2
dict3[3]='farmand'
print(dict3)
print(type(dict3))
print(dict3.values())

#konvertere liste til dictionary
x = (1,'a',2,'b',3,'c') 
d={x[i]:x[i+1] for i in range(0,len(x),2)}
print (d)

#merge lists to dict
a=[5,6,7]
b=['a1','b1','c1']
dmerge={a[i]:b[i] for i in range(0,len(a))}
print(dmerge)