# Function to take input from the user and return the number
def get_number():
    return int(input("Enter a number (0 to exit): "))

# Function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Function to calculate the power of a number
def power(base, exp=2):
    return base ** exp

# Function to display the result
def show_result(num):

    # Check whether the number is even or odd
    if is_even(num):
        print(num, "is Even")
    else:
        print(num, "is Odd")

    # Display the square of the number
    print("Square:", power(num))

# Use while loop to repeatedly ask for numbers
while True:

    # Get input from the user
    number = get_number()

    # Stop the program if the user enters 0
    if number == 0:
        print("Program ended.")
        break

    # Show the result                                                                         
    show_result(number)























































"""# Global variable
total = 0

# Function to add a value to the global variable total
def add_value(x):

    # Use the global keyword to modify the global variable
    global total

    # Local variable
    local_num = x

    # Add x to total
    total += x

    # Print the local variable inside the function
    print("Local variable inside function:", local_num)

# Call the function multiple times
add_value(10)
print("Total after first call:", total)

add_value(20)
print("Total after second call:", total)

add_value(30)
print("Total after third call:", total)

# Trying to access a local variable outside the function
# This will cause an error because local_num exists only inside add_value()
print(local_num)






# Recursive function to calculate the factorial of a number
def factorial(n):

    # Base case:
    # The factorial of 0 is 1, so stop recursion here
    if n == 0:
        return 1

    # Recursive case:
    # Multiply n by the factorial of (n - 1)
    return n * factorial(n - 1)

# Take input from the user
num = int(input("Enter a number: "))

# Call the function and store the result
result = factorial(num)

# Display the factorial result
print("Factorial:", result)

# Base case is the condition that tells a recursive function when to stop calling itself





# Recursive function to print numbers from n down to 1
def countdown(n) :

    # Base condition : if n becomes 0
    if n == 0 :
        return
    
    # print the current value of n
    print(n)
    # Decreased the value of n by 1
    countdown(n - 1)

# Call the function
countdown(10)






# Function to calculate square of a number
def square(num) :
    return num ** 2

# Function to calculate cube of a number
def cube(num) :
    return num ** 3

# Ask user to enter a number
user_num = int(input("Enter a number :"))

# call the functions and display the result
print("Square :", square(user_num))
print("Cube :", cube(user_num))
                                                                      





# Define a function with parameters
def student_info(name, age) :

    print("Name :",name)
    print("Age :",age)

# Call the function with positional arguments
student_info("Tanvi", 21)

# Call the function with keyword arguments
student_info(age=20, name="Neelam")

#The Difference:
# Positional arguments must be in the correct order (first, second, third).
# Keyword arguments use labels, so you can put them in any order you want.






# Define the function with parameters
def calculate_sum (a,b) :
    
    # 'return' sends the answer back without printing it on the screen
    return a+b

# Call the function with arguments and store the result in variable
total = calculate_sum(20,10)
#Print the final result
print(total)

# return - Stores the result so the program can use it later
# Print() - Only shows the result on the screen.

 



# Define a function with default parameter 
def show_message(message = "Hello"):
    print(message)

# Call function without an argument   
show_message()
# Call function with different message
show_message("Welcome")

# Benefits of default parameters :
# They give a backup value so the code doesn't crash if we leave it empty.





# Define a function
def greet(name) :
   
    print("Hello," + name + "! welcome back")

# Call the function with own name
greet("Tanvi")

# Call the function with different name
greet("Siya")





# Why Functions are useful?
# Functions are useful because they let us reuse the code and keep code orgranized

# Define a function
def welcome() :
    print("Welcome to python programming!")

#Call the function
welcome()"""