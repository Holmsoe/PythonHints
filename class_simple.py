class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Student({}, {})".format(self.name, self.age)

adam = Student('Adam Smith', 22)

print(adam.name)
print(adam.age)

#Change the object to content in textform.
#Make use of --str--(self)
print(adam)