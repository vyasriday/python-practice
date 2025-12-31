age = "age"
student = {
  "name": "Hridayesh Sharma",
  age: 21,
  "semester": "III",
  "stream": "Computer Science",
  21: "age"
}

print(student["name"])
print(student[21])
age = student["age"]
if student.get("year"):
  print(student["year"])
else:
  print("Key does not exist")

for (key, value) in student.items():
  print(key, ":" , value)
movies = {
  "Inception": "7:00 PM",
  "The Matrix": "8:30 PM",
  "Interstellar": "6:00 PM",
  "Pulp Fiction": "9:00 PM",
  "The Shawshank Redemption": "7:30 PM",
  "Forrest Gump": "8:00 PM",
  "The Dark Knight": "9:30 PM",
  "Gladiator": "7:15 PM",
  "Titanic": "6:30 PM",
  "Avatar": "8:45 PM"
}

print("Currently Available Movies.")
for movie in movies.keys():
  print(movie)

# for key in movies:
  # print(key)
userMovie = input("Pleaes enter the name of movie you want to check the show for.")

showTime = movies.get(userMovie)
print(showTime)
if showTime:
  print("Available show time is at", movies[userMovie])
else:
  print(userMovie, "is not available")

menu = {
  "breakfast": ["Eggs", "Toast", "Cereal", "Fruit", "Yogurt"],
  "lunch": ["Sandwich", "Salad", "Pasta", "Fruit", "Juice"],
  "dinner": ["Steak", "Vegetables", "Rice", "Pasta", "Soup"]
}

# take a user input about which item in which menu he wants to check. If availble return available else return not in menu today
userMenuQuery = input("Which menu would you like to check, breakfast, lunch or dinner? ")
nextLineSentence = "What dish would you like to check in " + userMenuQuery + " "
userItemQuery = input(nextLineSentence)
isItemAvailable = False
print(userMenuQuery, userItemQuery)

for item in menu.get(userMenuQuery):
  if item == userItemQuery:
    isItemAvailable = True
    break

if isItemAvailable:
  print("Available")
else:
  print("Sorry, we are not serving it today.")
  for (item, menu) in menu.items():
    print(item, ":", menu)
  

  
# for key in menu:
#   print("Options available for", key)
#   for item in menu[key]:
#     print(item)