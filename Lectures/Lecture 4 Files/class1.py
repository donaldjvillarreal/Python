#Person class definition.
class Person:
    #Object initialization function.
    def __init__(self):
        #Set a default object attribute.
        self.age = 0
        


person1 = Person()
person2 = Person()
person1.age += 2
print(person1.age)
print(person2.age)
