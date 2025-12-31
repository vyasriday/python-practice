# TODO

class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_details(self):
    return {
      "age":self.age,
      "name": self.name
    }

class Dog(Animal):
  def __init__(self, name, age, breed):
    super().__init__(name, age)
    self.breed = breed
  
  def get_details(self):
    dog = super().get_details()
    dog["breed"] = self.breed
    return dog
  

indie = Dog("Sheru", 4, "Indie")
print(indie)
print(indie.get_details())