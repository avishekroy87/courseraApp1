import typing
hotel_room = 100
tax = hotel_room * 0.8
total_cost = hotel_room + tax
room_guests = 4
share_per_guests = total_cost / room_guests

print(f"Guests: {room_guests}")
print(f"Total cost per person: " + str(share_per_guests))

# Module 2

def lucky_number(input):
    print("Your lucky number is " + str( len(input) * 2))

lucky_number('Aaron')
from traceback import print_tb


# 1) Complete the code to return the result of the conversion
def convert_distance(km):
	m = km * 1000  # exactly 1000 meters in 1 kilometer
	return m


# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above


my_trip_kilometers = 55


# 2) Convert my_trip_kilometers to meters by calling the function above
my_trip_meters = convert_distance(my_trip_kilometers)


# 3) Fill in the blank to print the result of converting my_trip_kilometers
print("The distance in meters is " + str(my_trip_meters))




def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)

print_seconds(1,2,3)
#output will print to the screen

def compare_strings(first_string, second_string):
    if len(first_string) > len(second_string):
        print("From the two strings First string is longer than second string")
    else:
        print("From the two strings Second string is longer than first string")


compare_strings('Jonnny', 'Dorr')

name = "Marjery"
home_address = "1234 Mockingbird Lane"
print(name + " lives at her home address of " + home_address)
# Should print "Marjery lives at her home address of 1234 Mockingbird Lane"


def speeding_ticket(speed):
    if (speed >= 85 ):
        ticket = "Reckless Driving"
    elif (speed > 65 and speed < 85 ):
        ticket = "Speeding"
    else:
        ticket = "Safe"
    return ticket


print(speeding_ticket(87)) # Should print Reckless Driving
print(speeding_ticket(66)) # Should print Speeding
print(speeding_ticket(65)) # Should print Safe
print(speeding_ticket(85)) # Should print Reckless Driving
print(speeding_ticket(35)) # Should print Safe
print(speeding_ticket(77)) # Should print Speeding





def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position


print(letter_translator("a")) # Should print 1
print(letter_translator("b")) # Should print 2
print(letter_translator("c")) # Should print 3
print(letter_translator("d")) # Should print 4
print(letter_translator("e")) # Should print unknown
print(letter_translator("A")) # Should print unknown
print(letter_translator("")) # Should print unknown




def return_nonnegative(first_num, second_num):
    if first_num > second_num:
        result = first_num - second_num
    else:
        result = second_num - first_num
    return result


print(return_nonnegative(5, 5)) # Should print 0
print(return_nonnegative(4, 5)) # Should print 1
print(return_nonnegative(5, 3)) # Should print 2
print(return_nonnegative(2, 5)) # Should print 3
print(return_nonnegative(5, 0)) # Should print 5
print(return_nonnegative(0, 5)) # Should print 5



def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif temp > 50 and temp <= 65:
        clothing = "Sweatshirt"
    elif temp > 32 and temp <= 50:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat



def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement

print(complementary_color("blue")) # Should print orange
print(complementary_color("yellow")) # Should print purple
print(complementary_color("red")) # Should print green
print(complementary_color("black")) # Should print unknown
print(complementary_color("Blue")) # Should print unknown
print(complementary_color("")) # Should print unknown


def difference(x, y):
    z = x - y
    return z


print(difference(5, 3))


print(((10 >= 5*2) and (10 <= 5*2)))



def safe_division(numerator, denominator):
    # Complete the if block to catch any "denominator" variables
    # that are equal to 0.
    if denominator == 0:
        result = 0
    else:
        # Complete the division equation.
        result = numerator/denominator
    return result


print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0