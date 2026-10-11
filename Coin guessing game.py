import random
print("Welcome to the coin guessing game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2.Using random.randint()")
choice = input("Enter your choice (1 or 2): \n")
if choice == "1":
  random_number = random.random()
  if random_number >= 0.5:
    computer_result = "Heads"
  else:
    computer_result = "Tails"
elif choice == "2":
  if random.randint(0,1) == 0:
    computer_result = "Heads"
  else:
    computer_result = "Tails"
else:
  print("Invalid choice. Please enter 1 or 2.")

user_choice = input("Enter your guess (Heads or Tails): \n")
if user_choice.lower() == computer_result.lower():
  print ("Congratulations! You won!.")
else:
  print("Sorry ! You lost.")
