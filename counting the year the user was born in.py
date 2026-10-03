str_age= input("How old are you: \n")
int_age= int(str_age)
int_year= 2026 - int_age
str_year= str(int_year)
print(" You were born in the year " + str_year)    
# using f string
str_age = input(" How old are you: \n")
int_age= int(str_age)
year= 2026 - int_age
print(f"You were born in the year: {year}")
