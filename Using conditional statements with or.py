area = input("Chose an area: (Cairo), (Alexandria) or (Tanta): \n")
if area.lower() == "cairo" or area.lower() == "alexandria" or area.lower() == "tanta":
  print(f"{area} is in our list.")
else:
  print(f"{area} isn't in our list.")
