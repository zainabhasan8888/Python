library = []
first_book = input("Enter the name of a book you own: \n")
second_book = input("Enter the name of another book you own ( or press enter to skip): \n")
library.append(first_book)
if second_book:
  library.append(second_book)
  print(f"Your library list is : {library}")
else:
   print(f"Your library list is : {library}")
wish_list = []
first_wish = input("Enter the name of a book you want to read in the future: \n")
wish_list.append(first_wish)
second_wish = input("Enter another name of a book you want to read in the future? (or press enter to skip): \n")
if second_wish:
  wish_list.append(second_wish)
  print(f"Your wish list is: {wish_list}")
else:
  print(f"Your wish list is: {wish_list}")
acquired = []
acquired_book = input(" Enter the name of a book from you wishlist that you already acquired (or press enter to skip): \n")
if acquired_book:
  acquired.append(acquired_book)
  wish_list.remove(acquired_book)
  print(f" Your acquired books list: {acquired}")
  print(f" your updated wish list is: {wish_list}")
else:
  print(" your acquired books list: {acquired}")

donations = []
donated_book = input("Enter a name of a book from your library you want to donate? (or press enter to skip): \n")
if donated_book:
  donations.append(donated_book)
  library.remove(donated_book)
  print(f"your donations list {donations}")
  print(f"your updated library list {library}")
else:
  print(" your library list is : {library}")

final_library = library + wish_list
print(f"your final library list is : {final_library}")
