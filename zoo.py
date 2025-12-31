from animal import Animal

class Zoo:
  def __init__(self):
    self.animals = []
  
  def add_animal(self, animal):
    self.animals.append(animal)
  
  def add_animals(self, animals):
    for animal in animals:
      self.animals.append(animal)

  def get_animals(self):
    for animal in self.animals:
      animal.display_animal()

zoo = Zoo()
dog = Animal("Lion", 8)
cat = Animal("Cat", 4)
monkey = Animal("Monkey", 18)
zoo.add_animals([dog, cat, monkey])
zoo.get_animals()

