class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def isAbove_18(self):
        return self.age>18

p1 = Person("Asif","Hasan",24)
p2 = Person("Adib","Hasan",34)
print(p1.isAbove_18())
print(p1.first_name+" "+ p1.last_name+" "+str(p1.age)+" age is above 18? "+ str(p1.isAbove_18()))
print(p2.first_name+" "+ p2.last_name+" "+str(p2.age)+" age is above 18? "+ str(p2.isAbove_18()))
