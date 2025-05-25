x = 0
while x < 5:
    print("Not there anything yet" + str(x))
    x = x + 1

print("x= " + str(x))

#Code2

def attemp_counter(input):
    input = 1;
    while input < 5:
        print("Attempt " + str(input))
        input = input + 1
    print("Terminate")

attemp_counter(5)

def count_down(start_number):
  while (start_number > 0):
    print(start_number)
    start_number -= 1
  print("Zero!")

count_down(3)




def print_range(start, end):
    # Loop through the numbers from start to end
    while start <= end:
        print( str(start))
        start +=  1


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)


def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?
    while number % 2 == 0:
        number += 1
        number = number / 2
        break
    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    if number == 1:
        return True
    return False


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


def sum_of_integers(n):
  if n < 1:
    return 0

  i = 1
  sum = 1
  while n > 1:
    i += 1
    sum = sum + i
    return sum


print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15


def is_power_of_two(number):
    # Handle non-positive numbers
    if number <= 0:
        return False
    # Check if number is a power of 2
    while number % 2 == 0:
        number = number / 2
    return number == 1

# Test calls
print(is_power_of_two(0))  # False
print(is_power_of_two(1))  # True
print(is_power_of_two(8))  # True
print(is_power_of_two(9))  # False