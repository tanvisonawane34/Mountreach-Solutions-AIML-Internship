#Ask user to enter a number
#define data type int to allow integers 
num = int(input("Enter a number: "))

#Check if number is greater than 100
#Add colon after the condition
if num > 100 :
    print("Large number")

#Check if the number is greater than 50
#Add colon after the condition
elif num > 50 :
    # Give proper indensation
    print("Medium number")

#Add colon after else
else :
    # Give proper indensation
    print("Small number")

#Count starts from 1
count = 1

# Loop runs while count is less than 10
while count < 10:

    # Print current value of count
    print(count)

    # Increase count by 1 to avoid infinite loop
    count = count + 1















































"""# Menu driven calculator using while loop

while True:

    # Display menu repeatedly
    print("\n----- MENU -----")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exit")
        break

    # Taking two numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        # Checking division by zero
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", num1 / num2)

    else:
        # If invalid choice entered
        print("Invalid choice")

        



# Loop from 1 to 50
for i in range(1, 41):
    
    # Check if the number is divisible by 3 & 5
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")

    # Check if the number is divisible by 3
    elif i % 3 == 0 :
        print("Fizz")
    
    #Check if the number is divisible by 5
    elif i % 5 == 0 :
        print("Buzz")

    #If not divisible by 3 & 5, print the number itself
    else :
        print(i)
    
    
        


#Program to give weather advice based on temperature and rain

# Take input from user
temp = int(input("Enter a temperature :"))
is_raining = (input("Is it raining? :"))

#Check if temperature is greater than 30
if temp > 30 :

    #Check if it is raining or not
    if is_raining == "no" :
        print("Hot day, wear light clothes")
    else :
        print("Hot and rainy, carry umbrella")

#Check if temperature is less than 15
elif temp < 15:
    if is_raining == "yes" :

        print("Cold and rainy,Wear jacket and take umbrella")
    else :
        print("Cold weather, wear warm clothes")

#For all other cases
else :
    print("Weather is pleasant, Dress comfortably")



            




# Program to keep accepting positive numbers from the user
# and calculate their total sum

total = 0
while True :

    #Take input from user
    num = int(input("Enter a positive no. :"))

    #Check if the number is negative or 0
    if num <= 0 :
        print("Total sum :", total)
        #Exit the loop
        break

    # Add the entered positive number to the tota
    total = total + num






# Print nos from 1 to 20 with their cubes
i = 1

# Continue looping till i becomes less than or equal to 20
while i<=20 :
     
    #Calculate the cube of current no.
    cube = i ** 3

    print("Number =",i, "Cube =",cube)

    #increment the value of i by 1
    i = i+1
    # The loop continues until the i becomes greater than 20








# Print all nos from 1 to 30

#loop starts from 1
i = 1

# range(30) generates nos from 0 to 29
for i in range(30) :

    # The number is incremented by 1
    print(i + 1)



    
    
# Print odd nos from 1 to 50
i = 1
for i in range(50) :
    # Checks whether the number is odd
    if i % 2 != 0 :
        print(i)

        




# Print sum of nos from 1 to 15

#Initialize sum with 0
sum = 0
# Generates nos from 0 to 14
for i in range(15):

    # Add numbers from 1 to 15
    sum = sum + (i + 1)

# Display the final sum
print("Sum : ",sum)

# range() is used to specify the numbers that the loop will use.





# Program to assign grades based on marks 

# Ask the user to enter marks
marks = float(input("Enter the marks :"))

# Check the marks and assign the grades accordingly
if marks >= 90 :
    print("Grade A - Excellent")

elif marks >= 75 :
    print("Grade B - Good")

elif marks >= 60 :
    print("Grade C - Average")

elif marks >= 40 :
    print("Grade D - Pass")

else :
    print("Fail")



    

# Program to check if the given no. is even or odd

# Take input from user
num = int(input("Enter a number :"))

 # Check if the number is divisible by 2
if num % 2 == 0 :
    # If remainder is 0, the number is even
    print("The number is even")
else :
    # If remainder is not 0, the number is odd
    print("The number is odd")





# Program to check voting eligibility

# Take the input from user
age = int(input("Enter your age :"))

# Check the condition
if age >= 18 :

    # Display the message if the condition is true
    print ("You are Eligible to vote")"""
