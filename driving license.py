age = int(input("How old are you? \n"))
license = input("Do you have a license? Answer Yes or No? \n")
if age >= 18 and license.lower() == "yes":
  print("You can drive.")
else:
  print("Sorry, you can't drive.")
