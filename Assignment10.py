# Simple Library Management System

# Create Book class
class Book:

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    # Issue book
    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("\nBook Issued Successfully!")
        else:
            print("Book is already Issued.")

    # Return book
    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("\nBook Returned Successfully!")
        else:
            print("Book is already Available.")

    # Show book details
    def show_info(self):
        print("Title :", self.title)
        print("Author :", self.author)
        print("Status :", self.status)
        print()
# List to store books
books = []

# Menu
while True:

    print("\n----- LIBRARY MENU -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # Add Book
    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        b = Book(title, author)
        books.append(b)

        print("\nBook Added Successfully!")

    # Issue Book
    elif choice == "2":
        title = input("Enter Book Title to Issue: ")

        found = False

        for book in books:
            if book.title == title:
                book.issue_book()
                found = True
                break

        if found == False:
            print("Book Not Found.")

    # Return Book
    elif choice == "3":
        title = input("Enter Book Title to Return: ")

        found = False

        for book in books:
            if book.title == title:
                book.return_book()
                found = True
                break

        if found == False:
            print("\nBook Not Found")

    # Show All Books
    elif choice == "4":

        if len(books) == 0:
            print("\nNo Books Available")

        else:
            for book in books:
                book.show_info()

    # Exit
    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice")
















































"""# Person Program

# Create class
class Person:

    # Constructor
    # Fixed: Added 'self' as the first parameter
    def __init__(self, name, age):

        # Fixed: Used self to store values in the object
        self.name = name
        self.age = age

    # Method to introduce
    # Fixed: Added 'self' as the parameter
    def introduce(self):

        # Fixed: Used self.name and self.age inside print()
        print("My name is", self.name, "and I am", self.age, "years old.")


# Creating object
p1 = Person("Tanvi", 21)

# Calling method
p1.introduce()








# Player Program

# Create class
class Player:

    # Constructor
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    # Increase score
    def increase_score(self, points):
        self.score = self.score + points
        print("Score Increased")

    # Increase level
    def level_up(self):
        self.level = self.level + 1
        print("Level Up!")

    # Show player details
    def show_progress(self):
        print("Player Name :", self.name)
        print("Score :", self.score)
        print("Level :", self.level)

# Creating object
p1 = Player("Riddhi", 100, 1)

# Show progress
p1.show_progress()

# Increase score
p1.increase_score(50)
p1.show_progress()

# Increase level
p1.level_up()
p1.show_progress()                                                    

# Increase score again
p1.increase_score(30)
p1.show_progress()

# Increase level again
p1.level_up()
p1.show_progress()






# Rectangle Program

# Create class
class Rectangle:

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Find area
    def area(self):
        return self.length * self.width

    # Find perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Display details
    def display(self):
        print("\nLength :", self.length)
        print("Width :", self.width)
        print("Area :", self.area())
        print("Perimeter :", self.perimeter())


# Take input from user
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

# Create object
r1 = Rectangle(length, width)

# Display results
r1.display()






# Mobile Phone Program
# Create class
class MobilePhone:

    # Constructor
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    # Charge the phone
    def charge(self, percent):
        self.battery_percentage = self.battery_percentage + percent
        print("Phone Charged")

    # Use the phone
    def use_phone(self, minutes):
        self.battery_percentage = self.battery_percentage - (minutes // 10)
        print("Phone Used")

    # Show phone details
    def show_status(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Battery :", self.battery_percentage, "%")
        print()

# Creating object
phone1 = MobilePhone("Samsung", "Galaxy A15", 80)

# Show current status
phone1.show_status()

# Charge phone
phone1.charge(10)
phone1.show_status()

# Use phone for 30 minutes
phone1.use_phone(30)
phone1.show_status()







# Employee Program
# Create class
class Employee:

    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to show employee details
    def display_details(self):
        print("Employee Name :", self.name)
        print("Salary :", self.salary)

    # Method to increase salary
    def give_raise(self, amount):
        self.salary = self.salary + amount
        print("New Salary :", self.salary)

    # Method to calculate yearly bonus
    def yearly_bonus(self):
        return self.salary * 10 / 100

# Creating object
e1 = Employee("Tanvi", 30000)

# Display details
e1.display_details()

# Give salary raise
e1.give_raise(5000)

# Show yearly bonus
print("Yearly Bonus :", e1.yearly_bonus()) 







# Student Grade Program

# Create class
class Student:

    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to Calculate grade
    def calculate_grade(self):
        # Checking the condition
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

    # Method to show student details
    def show_details(self):
        print("Name :", self.name)
        print("Marks :", self.marks)
        print("Grade :", self.calculate_grade())

# Creating objects
s1 = Student("Tanvi", 75)
s2 = Student("Neelam", 35)
s3 = Student("Riddhi", 48)

# Display details
s1.show_details()
s2.show_details()
s3.show_details()






# Bank Account Program

# Create class
class BankAccount:

    # Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # To add money
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Money Deposited")

    # To withdraw money
    def withdraw(self, amount):

        # Withdraw only if balance is sufficient
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Money Withdraw Succesfully!")
        else:
            print("Not enough balance")

    # Show balance
    def show_balance(self):
        print("Account Holder :", self.account_holder)
        print("Current Balance :", self.balance)
        
# Creating objects
acc = BankAccount("Tanvi", 6000)

acc.show_balance()
# Deposit money
acc.deposit(1000)
acc.show_balance()

# Withdraw money
acc.withdraw(2000)
acc.show_balance()






# Program using __init__ constructor

# Creating a class
class Book:

    # init Constructor 
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book information
    def show_details(self):
        print("Book Title :", self.title)
        print("Author     :", self.author)
        print("Price      :", self.price)
        
# Creating first book object
book1 = Book("Harry Potter", "J. K. Rowling", 500)

# Creating second book object
book2 = Book("The Jungle Book", "Rudyard Kipling", 350)

# To Displaying details of first book
book1.show_details()

# To Displaying details of second book
book2.show_details()






# Program to create a Car class and objects

# Creating a class
class Car:

    # Constructor to initialize brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to print car details
    def display_info(self):
        print("Car Brand :", self.brand)
        print("Car Model :", self.model)
        print()
        
# Creating a first object
car1 = Car("Toyota", "Fortuner")

# Creating a second object
car2 = Car("Hyundai", "Creta")

# Calling the method for first object
car1.display_info()

# Calling the method for second object
car2.display_info()"""