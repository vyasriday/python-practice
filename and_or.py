# write a program to print kid if below 18, adult if age is b/w 18 to 25, old if b/w 25 to 40 and very old if b/w 40 to 60. If none then print dead.

age = int(input("Enter your age: "))

if age < 1:
  print("Age can not be below 1")
elif (age > 1 and age < 18):
  print("Kid")
elif (age >= 18 and age < 25):
  print("Adult")
elif (age >= 25 and age < 40):
  print("Old")
elif (age >= 40 and age < 60):
  print("Very Old")
else:
  print("You are dead")

name = input("Enter your name: ")

if name == "Hridayesh" or name == "Khushboo":
  print("Full name is " + name + " Sharma")
elif name == "Vinay" or name == "Pushpa":
  print("Full name is " + name + " Singh")
else:
  print("Get a different name")

value = int(input("Enter any number b/w 1 to 10: "))

if not (value > 10):
  print("Value is under 10")
else:
  print("Value is greater than 10")

