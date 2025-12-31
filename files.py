import os
# Take user input about what acronym they want to check
# Open file and check if such acronym exists in file
# If yes return it else return not found message to the user

lookup = input("What is the acronym that you are looking for? ")
# with automatically manages the file closing and resource management but to manage any exception you need to wrap it in try except
try:
  with open("texts/acronyms.txt") as file:
    for line in file:
      if lookup in line:
        print(line.split("=")[1])
        break  
except FileNotFoundError as e:
  print("File not found", e)
  
#. OTHER WAY TO OPEN FILES
try:
  file = open("texts/acronyms.txt")
  result = file.readlines()
  print(result)
except:
  print("Error occured in opening the file")
finally:
  file.close()

  
user_ac = input("Enter your own acronyms: ")
user_ac_def = input("Enter the definition of the acronym: ")

with open("texts/acronyms.txt", "a") as file:
  file.write("\n" + user_ac +  "=" + user_ac_def)
  
try:
  os.mkdir("new_folder")
except:
  print("Error occured")