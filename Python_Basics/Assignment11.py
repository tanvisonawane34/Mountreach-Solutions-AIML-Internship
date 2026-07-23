# Simple Calculator using exception handling

# While loop to display menu repeatedly
while True :

    print("\n-------- Simple Calculator --------")
    print("\n1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")
    
    # Asking user to enter choice
    choice = input("\nEnter your choice : ")

    if choice == "5" :
            print("\nProgram Exited!")
            break
            
    if choice not in ("1","2","3","4","5") :
        print("Invalid Choice! Please enter the number between 1-5")

    else :
        # Try block
        try :
            # Taking inputs from user
            num1 = float(input("\nEnter first number : "))
            num2 = float(input("Enter second number : "))

            # Checking the condition
            if choice == "1":
                print("Addition : ",num1 + num2)

            elif choice == "2" :
                print("Subtraction : ", num1 - num2) 

            elif choice == "3" :
                print("Multiplication : ", num1*num2)

            elif choice == "4" :
                print("Division : ", num1 / num2)
        
        # Except block for value error
        except ValueError :
            print("Invalid Input! Please enter numeric values")
        
        # Except block to handle zero division error
        except ZeroDivisionError :
            print("Cannot divide by zero")
        
        # Finally block that always executes
        finally :
            print("Operation attempted.")





"""# Correcting the given code
try :
    num = int(input("Enter a number: ")) 
    result = 100 / num 
    print("Result:", result) 
    
except ValueError :
     print("Please enter a valid number")

except Exception: 
    print("Some error occurred")






# Program to handle multiple exceptions in one block

# Try block
try :
    # Taking input from user
    num = int(input("Enter a number : "))
    print("Division : ",100/num)

# Except block
except (ValueError, ZeroDivisionError) :
    print("Please enter a valid number. Division by zero is not allowed.")





# Program to check age

# Try block
try :
    # Taking input from user and converting to integer
    age = int(input("Enter your age : "))

    if age < 0 :
        raise ValueError("Age cannot be negative")

    # To display the age
    print("Age : ",age)

# Except block
except ValueError as e:
    print(e)


    
    

    
# Program using try, except, else and finally

# Try block
try:
    # Taking input from user
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Division:", num1 / num2)

# Except block for zero division error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Except block for value error
except ValueError:
    print("You have to enter a numeric value.")

# Else block
else:
    print("Division performed successfully!")

# Finally block
finally:
    print("Thank you for using the program!")


    
    
    
# Program using try, except and finally

# Try block
try:
    # Taking input from user
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Division:", num1 / num2)

# Except block for zero division error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Except block for value error
except ValueError:
    print("You have to enter a numeric value.")

# Finally block
finally:
    print("Program execution completed.")

# Finally block always executes whether an exception occurs or not






# Program using try, except and else

# Try block
try:
    # Taking input from user
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Division:", num1 / num2)

# Except block for zero division error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Except block for value error
except ValueError:
    print("You have to enter a numeric value.")

# Else block
else:
    print("Division performed successfully!")





    
# Program to handle the zero division error

# Try block
try :
    # Taking input from user
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    
    print("Division : ", num1/num2)
    
    # Converting string to integer
    a = input("\nEnter a number : ")
    number = int(a)
    print("Converted number : ",number)

# Except block for zero division error
except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")

# Except block for value error
except ValueError :
    print("You have to enter a numeric value")




    
# Program to handle the zero division error

# Try block
try :
    # Taking input from user
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    
    print("Division : ", num1/num2)

# Except block for zero division error
except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")

# Except block for value error
except ValueError :
    print("You have to enter a numeric value")






# Try-except program

# Try block
try :
    # Taking input from user
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("Division :",num1 / num2)

# Except block
except ValueError :
    print("\nYou have to enter a numeric value!")"""