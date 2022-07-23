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

print("************ Class Variable **************")

class Circle:
    pi =3.1416

    def __init__(self,redious):
        self.redious = redious
    
    def calc_circumference(self):
        return 2 * Circle.pi * self.redious

c1 = Circle(4)
print(c1.calc_circumference())
c2 = Circle(5)
print(c2.calc_circumference())

print("c1 is "+str(c1.calc_circumference()) +" c2 is "+str(c2.calc_circumference()))