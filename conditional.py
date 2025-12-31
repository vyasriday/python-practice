a = int(input("Enter first number "))
b = int(input("Enter second number "))
operator = input("Enter the operation ")

if operator == "+":
  print("Sum is ", a+b)
elif operator == "-":
  print("Subtraction is ",a-b)
elif operator == "*":
  print("Multiplication is " , a*b)
else:
  print("Division is " , a/b)