str_seconds = input("Enter the duration in seconds: \n")
int_seconds = int(str_seconds)
minutes = int_seconds // 60
hours = minutes // 60
remaining_seconds = int_seconds % 60
print(f" The duration is {hours} hours {minutes} minutes {remaining_seconds} seconds")
