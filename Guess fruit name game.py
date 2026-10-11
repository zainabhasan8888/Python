fruit_basket = ["apples", "oranges", "bananas"]
guess = input(" Guess the name of the fruits in the basket: \n").lower()
if guess in fruit_basket: 
  print("Good guess!")
else:
  print("Better luck next time.")
