class Student:
  # constructor fc. First argument is always self.
  def __init__(self, name, age):
    print("I am called with", self, age, name)
    self.name = name
    self.age = age
  # first argument to method is always self object
  def get_name(self):
    print(self)
    return self.name

st1 = Student("Hridayesh", 21)

print(st1.name)
print(st1.age)
print(st1.get_name())
st1.__init__("Ajay", 28)
print(st1.get_name())
