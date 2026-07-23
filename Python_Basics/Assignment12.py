# Q10
# Importing modules 
import math
import random
import time

# Creating empty dictionary
history = {}
# While loop to display menu
while True:

    print("\n--- SMART CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Random Number")
    print("7. View History")
    print("8. Exit")

    choice = input("\nEnter choice: ")

    try:

        # Addition
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            res = a + b
            print("Result:", res)

            current_time = time.ctime()
            history[current_time] = f"{a} + {b} = {res}"

        # Subtraction
        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            res = a - b
            print("Result:", res)

            current_time = time.ctime()
            history[current_time] = f"{a} - {b} = {res}"

        # Multiplication
        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            res = a * b
            print("Result:", res)

            current_time = time.ctime()
            history[current_time] = f"{a} * {b} = {res}"

        # Division
        elif choice == "4":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            res = a / b
            print("Result:", res)

            current_time = time.ctime()
            history[current_time] = f"{a} / {b} = {res}"

        # Square root of a number
        elif choice == "5":
            a = float(input("Enter number: "))
            res = math.sqrt(a)
            print("Result:", res)

            current_time = time.ctime()
            history[current_time] = f"sqrt({a}) = {res}"

        # Random number
        elif choice == "6":
            a = int(input("Start: "))
            b = int(input("End: "))
            res = random.randint(a, b)
            print("Random Number:", res)

            current_time = time.ctime()
            history[current_time] = f"random({a},{b}) = {res}"

        # to view history
        elif choice == "7":
            if len(history) == 0:
                print("No history found")
            else:
                print("\n--- HISTORY ---")
                for t, val in history.items():
                    print(t, ":", val)

        # Exiting the program
        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")
    # Except block
    except:
        print("Something went wrong. Please enter valid input.")





"""# Q9
# Import math module
import math

try:

    # Take sentence from the user
    sentence = input("Enter a sentence: ")

    # Split the sentence into words
    words = sentence.split()

    # Store unique words in a set
    unique_words = set(words)

    # Sort the unique words
    sorted_words = sorted(unique_words)

    print("\nUnique Words:")
    for word in sorted_words:
        print(word)

    # Count unique words
    total = len(unique_words)

    # Print square of total unique words
    print("\nSquare of Total Unique Words:", math.pow(total, 2))

except Exception:
    print("Something went wrong")






# Q8
# Create Employee class
class Employee:

    # Constructor to initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name

        # Store department and salary in a tuple
        self.details = (department, salary)

    # Method to display employee details
    def show_details(self):
        print("\nEmployee ID :", self.emp_id)
        print("Name :", self.name)
        print("Department :", self.details[0])
        print("Salary :", self.details[1])


# Empty dictionary to store employee objects
employees = {}

# Create 3 employee objects
emp1 = Employee(101, "Apurva", "HR", 30000)
emp2 = Employee(102, "Tanvi", "IT", 45000)
emp3 = Employee(103, "Riddhi", "Sales", 35000)

# Store employee objects in dictionary
employees[emp1.emp_id] = emp1
employees[emp2.emp_id] = emp2
employees[emp3.emp_id] = emp3

# Display all employee details
print("Employee Details :")

for emp_id, emp in employees.items():
    emp.show_details()







# Q7
# Lambda function to find square of a number
square = lambda x: x * x

# Empty list to store squares
square_list = []

try:

    # Generate numbers from 1 to 20
    for num in range(1, 21):

        # Find square using lambda function
        result = square(num)

        # Store square in the list
        square_list.append(result)

    print("Squares of Numbers:")
    print(square_list)

    print("\nEven Squares:")

    # Print only even squares
    for i in square_list:
        if i % 2 == 0:
            print(i)

# Except block
except Exception:
    print("Something went wrong!")





# Q6
# Importing modules
import random
import math

# Empty set to store unique numbers
numbers = set()

try:
    # Take 10 numbers from the user
    for i in range(10):
        num = int(input("Enter a number: "))
        # Adding number to the set
        numbers.add(num)   

    # Convert set into tuple
    num_tuple = tuple(numbers)

    print("\nTuple:", num_tuple)

    # Print random numbers from the tuple
    print("\n3 Random Numbers:")
    random_numbers = random.sample(num_tuple, 3)
    print(random_numbers)

    # Find the sum of tuple elements
    total = sum(num_tuple)

    # Print square root of the sum
    print("\nSquare Root of Sum:", math.sqrt(total))

# Handles invalid input
except ValueError:
    print("Please enter numbers only")

# Handles error if there are less than 3 unique numbers
except:
    print("Not enough unique numbers to pick 3 random numbers")


    
    

    
# Q5   
# Create a function
def student_database() :

    # Empty dictionary to store student records
    students = {}

    # Loop to display menu
    while True:
        print("\n-------- STUDENT DATABASE -------")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        # Take user's choice
        choice = input("\nEnter your choice: ")

        if choice == "1":

            try:
                # Take student details from user
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                # Adding student record
                students.update({
                    roll: {
                        "name": name,
                        "age": age,
                        "city": city
                    }
                })

                print("\nStudent Added Successfully!")

            # Handles invalid input
            except ValueError:
                print("Invalid Input!")

        elif choice == "2":

            try:
                # Ask for roll number to search
                roll = int(input("Enter Roll Number: "))
                student = students.get(roll)

                # If student is found
                if student:
                    print("Name :", student["name"])
                    print("Age :", student["age"])
                    print("City :", student["city"])

                # If roll number does not exist
                else:
                    print("Student Not Found")

            # Handles invalid roll number input
            except ValueError:
                print("Invalid Roll Number!")

        elif choice == "3":

            # Check if dictionary is empty
            if students == {}:
                print("No Student Records")

            else:
                # Display all student records
                for roll, student in students.items():
                    print("\nRoll Number :", roll)
                    print("Name :", student["name"])
                    print("Age :", student["age"])
                    print("City :", student["city"])

        elif choice == "4":
            print("Thank You!")
            break
        # If user enters an invalid menu choice
        else:
            print("Invalid Choice")

# Calling a function
student_database()






# Q4
# Create a class
class Student :
    
    # Constructor to initialize details
    def __init__(self, name, roll_no) :
        self.name = name
        self.rollno = roll_no
        # Empty list to store marks 
        self.marks_list = []

    # Method to add marks in the list
    def add_mark(self,mark) :
        try :
            mark = int(mark)
            self.marks_list.append(mark)
        except ValueError :
            print("Invalid marks")

    # method to return average
    def get_average(self) :
        return sum(self.marks_list)/len(self.marks_list)
    
    # To display student details
    def display_info(self) :
        print("\nName : ", self.name)
        print("Roll no : ", self.rollno)
        print("Marks : ",self.marks_list)
        print("Average : ",self.get_average())

# Creating a object        
s1 = Student("Tanvi",53)

for i in range(5) :
    mark = (input("Enter a marks : "))
    s1.add_mark(mark)

# Calling a function
s1.display_info()






# Q3
# Create a function
def manage_marks () :
    # Empty list to store marks
    marks = []
    
    # Try block
    try :
        # Using for loop to print marks of 5 subjects
        for i in range(5) :
            m = int(input(f"Enter marks of sub {i+1} : "))
            # Adding the marks to the list
            marks.append(m)

    # Except block to handle the error    
    except ValueError :
        print("Please enter a numeric value!")
        return
    
    # To print average 
    print("\nAverage : ",sum(marks) / len(marks))
    # To print lowest marks
    print("Lowest marks : ",min(marks))
    # To pritn highest marks
    print("Highest marks : ",max(marks))
    
    # To print the list in descending order
    marks.sort(reverse=True)
    print("\nDescending order : ",marks)

# Calling the function
manage_marks()
    
    




# Q2
# Create a function
def analyze_string(s) :
    
    # Checking if the string is empty
    if s == "" :
        print("String is empty")
        return
    
    # To display the length of the string
    print("Length of the string : ",len(s))
    
    # To print the string in reverse
    print("String in reverse : ",s[::-1])
    
    # Count and prints how many vowels
    count = 0
    s = s.lower()
    for i in s :
        if i in "aeiou":
            count += 1
    print("Number of Vowels : ",count)
    print()
    
    # For loop to print eachh character
    for i in range (len(s)) :
        
        # Printing positive and negative index
        print("Positive index :",i,
              "\tNegative Index :",i - len(s),
              "\tCharacter :", s[i] )

# Taking string from user 
s = input("\nEnter a string : ")
# Calling the function
analyze_string(s)"""
