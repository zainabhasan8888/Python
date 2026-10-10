import random
print("Welcome to the virtual coin toss game.")
input("Press Enter to start....")
random_number = random.random()
if random_number >= 0.5:
  print("Heads.")
else:
  print("Tails.")
