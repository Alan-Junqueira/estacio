from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirth(cls, name, age):
        return cls(name, date.today().year - age)

    @staticmethod
    def isAdult(age):
        return age >= 18

person1 = Person('João', 30)
person2 = Person.fromBirth('Maria', 2006)

print(person1.age)
print(person2.age)

print(Person.isAdult(17))