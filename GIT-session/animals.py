import sys

class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def speak(self):
    print("I am", self.name, "and I am", self.age, "years old")

class Cat(Animal):
  def __init__(self, name, age):
    super().__init_(name, age)
    self.type = 'cat'

  def speak(self):
    super().speak
    print("Meaowww! I'm a cat, you know?")
    print("Just another line added. We need modifies here")

class Dog(Animal):
  def __init__(self, name, age):
    super().__init_(name, age)
    self.type = 'dog'
    
  def speak(self):
    super().speak()
    print("Woof!")
    
if __name__ == "__main__":
  called_animal = Dog(sys.argv[1], sys.argv[2])
  called_animal.speak()