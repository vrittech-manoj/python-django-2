class Person:
    def __init__(self, name, age):
        self.__type = 'This is a private attribute.'
        self.name = name
        self.age = age

person = Person('John Doe', 30)
print(person.__type) 