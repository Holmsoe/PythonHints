
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        self.PrintName()
        
    def Name(self):
        return self.firstname + " " + self.lastname

    def PrintName(self):
        print("initialisering af Parent",self.firstname,self.lastname)
        

class Employee(Person):

    def __init__(self, first, last, staffnum):
        print("initialisering af child")
        #Person.__init__(self,first, last)   #Bemærk denne initialisering af parent i child
        super().__init__(first, last)      #Kalder også parent uanset navn
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
print("ugh")
y = Employee("Homer", "Simpson", "1007")

z=x.Name

print(z())
print(y.Name())
print(y.GetEmployee())
