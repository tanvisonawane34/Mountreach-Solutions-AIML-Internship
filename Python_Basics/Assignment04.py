# Import modules
import math
import random

# Lambda function to find square
square = lambda x: x ** x

# Function to calculate power
def power(base, exp):
    return math.pow(base, exp)

# Repeat until user chooses to exit
while True:

    print("\n1. Square")
    print("2. Power")
    print("3. Random Number")
    print("4. Exit")
    
    # Take input from user
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Square =", square(num))

    elif choice == 2:
        num = int(input("Enter a number: "))
        exp = int(input("Enter exponent: "))
        print("Power =", power(num, exp))

    elif choice == 3:
        print("Random Number =", random.randint(1, 100))

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")                                                            






# Code inside if __name__ == "__main__"
# runs only when the file is executed directly

# Define a function
def greet():
    print("Welcome to Python Programming!")

# This code runs only when the file is executed directly
if __name__ == "__main__":
    greet()



    
# Different ways of importing module
# Import the entire module
import math
print("Power of 2 raise to 4 :",math.pow(2,4))

# Import a specific function from math module
from math import sqrt
print("Square root of 3 :", math.sqrt(3))

# Import math with alias
import math as m
print("Factorial of 5 :",m.factorial(5))




# The random module is useful for generating random numbers
# Import the random module
import random

# Print random 5 numbers between 1 and 100
print("Random 5 numbers between 1 and 100 :")
for i in range(5) :
    print(random.randint(1,100))

# Print a random number between 50 and 150
print("Random number between 50 and 150 :")
print(random.randint(50,150))

# Print a random float-number between 0 and 1
print("Random float between 0 and 1 :")
print(random.random())





# The math module provides built-in mathematical functions
# It makes calculations easier and more efficient.

# Import the built-in math module
import math

# Ask the user to enter a number
num = float(input("Enter a number :"))

# Print the square root of a number
print("Square :",math.sqrt(num))

# Print the factorial of a number
if num >= 0 :
    print("Factorial :",math.factorial(int(num)))
else :
    print("Factorial is not possible for negative numbers")

# Print the floor value    
print("Floor value :",math.floor(num))
# Print the ceil value
print("Ceil value :",math.ceil(num))                                     





# Variable to store the total sum
total = 0

# Repeatedly ask the user for a number
while True:
    num = int(input("Enter a positive number: "))

    # Stop if the user enters 0 or a negative number
    if num <= 0:
        break

    # Add the number to the running total
    total += num

# Display the final sum
print("Total Sum =", total)






# For loop revision 
# Print nos from 1 to 25
print("Numbers from 1 to 25 :")
for i in range(1,26) :
    print(i)

# Sum of all numbers from 1 to 20
print("Sum of numbers from 1 to 20 :")
sum = 0
for i in range(1,21) :
    sum += i
print("Sum :", sum)

# Table of 5
print("Table of 5 :")
for i in range(1,11) :
    print("5 x",i, "=", 5 * i)
    
# We use a for loop to repeat a block of code instead of writing the same code repeatedly.
# It is used when the number of iterations is known.                                            





# Create a lambda function
add_three = lambda a,b,c : a+b+c

# Take input from user
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

# Display the final sum
print("Sum :",(add_three(a,b,c)))







# Lambda function
square = lambda x : x**2

# Ask the user to enter a number
num = int(input("Enter a number :"))
# Display the square of the number
print("Square : ",square(num))

# Define a function using def keyword
def square(x):
    return x**2

num = int(input("Enter a number :"))
print("Square :", square(num))

# Lambda Function:
# - Short and anonymous function
# - Used for simple one-line tasks
# - Returns the value by default

# Normal Function (def):
# - Named function.
# - Better for larger programs                                       
# - Uses return keyword to return a value"""