# 1 Object - a variable or a method with attributes
# 2 Class - a definition of an object's attributes and methods 


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# 3 Polymorphism - having one common name and many forms

num1 = 1
num2 = 2
print(num1+num2)

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)


# 4 Encapsulation - hiding attributes or methods as needed
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# 5 Inheritance - makes new object from parent attributes and methods

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  