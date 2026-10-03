str_length= input("please type length: \n")
str_width= input("please type width: \n")
str_price= input(" How much for 1 meter? \n")
length = float(str_length)
width = float(str_width)
price= float(str_price)
area = length*width
total_price= area*price
str_area = str(area)
str_total_price= str(total_price)
print( "The total area is:" + str_area)
print("The total price is:" + str_total_price)
