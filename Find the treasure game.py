choice = input("""
Welcome to my island!
There are two doors in front of you. a red door and a blue door.
which door do you want to open? \n 
""").lower()
if choice == "red":
  red_door = input("""
  Great! now yow entered a room.
  you found three boxes: white, black, green.
  which box do you open? \n """).lower()
  if red_door == "white":
    print("Oops! you opened a box filled with snakes! ")
  elif red_door == "black":
    print("Oops! you opened a box filled with spiders!")
  elif red_door == "green":
    print("Congratulations! you found the treasure!")
  else:
    print(" Invalid choice.")
elif choice == "blue":
  print(""" Oops! you chose the crocodile door.
 game over! """)
else:
  print("Invalid choice!")
