#define class

class Person:
    x = 10

#create object

person1 = Person()

#Class with init function. Init function same as constructor function

class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

class1 = MyClass("Ismail", "27")
print(class1.name)
print(class1.age)

#class with method

class MethodClass:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def description(self):
        x = "My name is "+ self.name + ".I am "+self.age +" years old."
        print(x)

method1 = MethodClass('Ismail','27')
method1.description()