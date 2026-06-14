# Name: Jose Rodriguez
# 5/22/2026
# Module 11.2 Assignment
# Recursive vs Non-Recursive Number Counter

# This program demonstrates the difference between a recursive
# function and a non-recursive function by printing the numbers
# from 1 up to and including a user-entered positive integer.

# Sources:
# W3Schools. (n.d.). Python recursion.
# https://www.w3schools.com/python/python_recursion.asp

# GeeksforGeeks. (2025, August 8). Python Tkinter geometry management.
# https://www.geeksforgeeks.org/python-tkinter-geometry-management/



# Recursive Function
def recursive_count(current_number, max_number):

# This recursive function prints numbers from 1 to max_number.

# Approach:
# The function prints the current number and then calls itself
# using the next number. The process continues until the current
# number becomes greater than the maximum number.

# Base Case:
# Stop recursion when current_number is greater than max_number.

# Base case to stop recursion
    if current_number > max_number:
        return

# Print the current number
    print(current_number)

# Recursive call using the next number
    recursive_count(current_number + 1, max_number)



# Non-Recursive Function

def non_recursive_count(max_number):

# This non-recursive function prints numbers from 1 to max_number.

# Approach:
# The function uses a for loop to count from 1 through the
# maximum number entered by the user.


# Loop through numbers from 1 to max_number
    for number in range(1, max_number + 1):
        print(number)



# Main Program


# Display program title
print("==========================================")
print(" Recursive vs Non-Recursive Counter ")
print("==========================================")



# Input Validation

# Continue asking the user until a valid positive integer is entered

while True:

    try:
        user_number = int(input("\nEnter a positive integer greater than 0: "))

        # Reject negative numbers and 0
        if user_number <= 0:
            print("ERROR: Number must be greater than 0.")

        else:
            # Exit loop if input is valid
            break

    except ValueError:
        # Handle non-integer input
        print("ERROR: Please enter a valid whole number.")




# Recursive Function Output

print("\n--- START Recursive Function ---")

recursive_count(1, user_number)

print("--- END Recursive Function ---")



# Non-Recursive Function Output

print("\n--- START Non-Recursive Function ---")

non_recursive_count(user_number)

print("--- END Non-Recursive Function ---")