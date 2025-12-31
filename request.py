import requests

URL = 'http://api.open-notify.org/astros.json'
response = requests.get(URL)
data = response.json()
people = data["people"]
totalPeople = data["number"]

print("People currently in space with their spacecrafts: ")
for person in people:
  print("Name: ", person["name"])
  print("Craft: ", person["craft"])
  print("\n")