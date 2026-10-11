colors = []
first_color = input("Add the first color you like: \n")
choice = input("Do you want to add more colors? Yes or No \n").lower()
colors.append(first_color)
if choice == "yes":
  second_color= input("Add the second color you like: \n")
  colors.append(second_color)
  print(colors)
elif choice == "no":
  print(colors)
else:
  print("Invalid input.")

