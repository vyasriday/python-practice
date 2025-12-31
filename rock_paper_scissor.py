import random

options = ["rock", "paper", "scissors"]
index = random.randint(0,2)
computer = options[index]
print(computer)
user = input("rock, papaer, scissor?: ")


if (user != "rock" and user != "paper" and user != "scissors"):
  print("Wrong option entered. Enter one of rock, paper or scissors.\n")

if(user == computer):
  print("It's a tie")

if user == "rock" and computer == "scissors":
  print ("USER WINS")
elif user == "paper" and computer == "scissors":
  print("COMPUTER WINS")
elif user == "scissors" and computer == "rock":
  print("COMPUTER WINS")
elif user == "rock" and computer == "paper":
  print("COMPUTER WINS")
elif user == "scissors" and computer == "paper":
  print("USER WINS")
elif user == "paper" and computer == "scissors":
  print("COMPUTER WINS")