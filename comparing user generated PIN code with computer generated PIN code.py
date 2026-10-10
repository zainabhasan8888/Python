import random
pin_code = random.randint(1000,9999)
user_input = int(input("Enter a 4-digit  PIN code: \n"))
if len(str(user_input)) > 4 or len(str(user_input)) < 4:
  print("Please enter 4-digit number.")
elif user_input == pin_code:
  print("Success! PIN code matched!")
else:
  print("Failure! PIN code didn't matched.")
  print(f"The computer generated this PIN code {pin_code1}")
