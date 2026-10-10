import random
print("Welcome to the virtual coin toss game.")
input("Press Enter to start....")
random_number = random.randint(0,1)
if random_number == 0:
  print("Heads.")
else:
  print("Tails.")
