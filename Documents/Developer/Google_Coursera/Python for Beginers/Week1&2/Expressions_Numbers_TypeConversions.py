# int + float type
print(7+8.5)

# This is pretty neat !
print("This "+"is "+"pretty "+"neat !")


# Area of a triangle ?
base = 6 
height = 3
area = (base*height)/2
print("Area of the triangle is : " + str(area))


# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests 
 
# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) 
# change a data type


# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + " , " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.




print("5 * 3 = " + str(5 * 3)) 
 
# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  



# By chatGPT
bill_amount = 47.28  # Bill amount in dollars
tip_percentage = 15  # Tip percentage

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount to pay (bill amount + tip amount)
total_amount = bill_amount + tip_amount

# Calculate each friend's share (total amount divided by 2)
each_person_share = total_amount / 2

# Print the result
print("Each person needs to pay:", each_person_share)


# ~ by Sohan Maity

bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total/2 # Divide "total" by number of friends dining
print("Each person needs to pay: " + str(share)) # Enter the required string and "share" 
# Hint: Remember to convert incompatible data types
