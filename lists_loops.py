choices = [1,2,3,4,5,6]
user_choice = int(input("Enter your choice: "))

if user_choice in choices:
  print("Your guess is from the list")
else:
  print("You selected out of list number")

family = [];
family.append("Hridayesh Sharma")
family.append("John Doe")
family.append("New Name")

print(family)

family.remove("New Name")
print(family)

family.append("Michael Sharma")
print(family)

del family[2]
print(family)

family.append("Shubh Sharma")
family.append("Vin Sharma")
family.append("Paperazi Sharma")

for member in family:
  print(member)


animals = ["lion", "elephant", "tiger", "giraffe", "zebra", "monkey", "bear", "penguin", "dolphin", "eagle"]

expenses = []
totalNoOfExpenses = int(input("What is the total no of expenses? "))
for i in range(totalNoOfExpenses):
  expense = input("Enter expense ")
  expenses.append(int(expense))
print("Total of all the expenses is", sum(expenses))

# even no upto certain no

user_input = int(input("What is the max no? "))

print("Even numbers upto", user_input)
for even in range(0, user_input, 2):
  print(even)

print("Odd numbers upto", user_input)
for odd in range(1,user_input, 2):
  print(odd)