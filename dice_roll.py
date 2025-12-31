import random

def dice_roll():
  random_int = random.randint(1,6)
  return random_int

def main():
  player1 = dice_roll()
  player2 = dice_roll()

  if player1 > player2:
    print("Player 1 wins")
  else:
    print("Player 2 wins")

main()