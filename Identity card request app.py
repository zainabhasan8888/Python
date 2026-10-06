identity = input("Are you Iraqi? answer Yes or No? \n").lower()
if identity == "yes":
  print("good, this is the first step.")
  age =int(input("How old are you? \n"))
  if age >= 18:
    print("You can have an Identity Card.")
  else:
    print("Sorry, you have to be 18 or older.")
    print("please try again when you're 18.")
else:
  print("Sorry, An Iraqi ID is given only to Iraqis.")
