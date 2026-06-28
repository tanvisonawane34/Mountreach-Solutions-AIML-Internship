# Student Management System

# Creating an empty dictionary
record = {}

while True:

    print("\n----- Student Management System -----")
    print("1. Add New Student")
    print("2. Update Marks")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Remove Student")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    # Add new student
    if choice == 1:
        roll = input("Enter Roll Number: ")
        s_name = input("Enter Student Name: ")
        s_age = input("Enter Age: ")
        s_marks = input("Enter Marks: ")

        record[roll] = {
            "Name": s_name,
            "Age": s_age,
            "Marks": s_marks
        }

        print("Student added successfully")

    # Update marks
    elif choice == 2:
        roll = input("Enter Roll Number: ")

        if roll in record:
            new_marks = input("Enter New Marks: ")
            record[roll].update({"Marks": new_marks})
            print("Marks updated successfully")
        else:
            print("Student not found")

    # Search student
    elif choice == 3:
        roll = input("Enter Roll Number: ")

        if roll in record:
            print("Student Details:")
            print(record.get(roll))
        else:
            print("Student not found")

    # Display all students
    elif choice == 4:

        if len(record) == 0:
            print("No student records found")
        else:
            print("Student Records:")
            for roll, details in record.items():
                print("Roll Number:", roll)
                print("Name:", details["Name"])
                print("Age:", details["Age"])
                print("Marks:", details["Marks"])
                print()

    # Remove student
    elif choice == 5:
        roll = input("Enter Roll Number: ")

        if roll in record:
            record.pop(roll)
            print("Student removed successfully")
        else:
            print("Student not found")

    # Exit
    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")



















































"""# Creating a dictionary

info = {}

# Taking input from the user
name = input("Enter a name: ")
phone_no = input("Enter a phone no.: ")
email = input("Enter an Email: ")

# Storing the details with name as the key
info[name] = {
    "Phone": phone_no,
    "Email": email
}

# Searching for a contact
search = input("\nEnter the name to search: ")

print("\nContact Details:")

if search in info:
    print(info.get(search))
else:
    print("Contact not found")

# Printing all contacts
print("\nAll Contacts:")
for name, details in info.items():
    print("Name:", name)
    print("Phone:", details["Phone"])
    print("Email:", details["Email"])






# fromkeys() and membership()

# Creating a dicitonary using fromkeys()
keys = ["Name","Age","City"]
d = dict.fromkeys(keys,None)

# Taking input from the user
d["Name"] = input("Enter your name: ")
d["Age"] = input("Enter your age: ")
d["City"] = input("Enter your city: ")

# Printing the dictionary
print(d)

# Checking if a key exists
key = input("Enter the key to check: ")

if key in d:
    print("Key is present")
else:
    print("Key is not present")


    
    

    
# copy() and setdefault()

# Creating a dictionary
d = {
    "a": 1,
    "b": 2
}

# Making a copy of the dictionary
copy_dict = d.copy()

# Adding a new key using setdefault()
d.setdefault("c", 3)

# Using setdefault() for an existing key
d.setdefault("a", 10)

# Printing the original dictionary
print("Original Dictionary:")
print(d)

# Printing the copied dictionary
print("\nCopied Dictionary:")
print(copy_dict)






# pop() and popitem()

# Creating a dictionary
student = {
    "name": "Tanvi",
    "age": 19,
    "city": "Mumbai",
    "marks": 92,
    "grade": "A"
}

# Removing items using popitem()
removed = student.popitem()
print("First removed item:",removed)
removed2 = student.popitem()
print("Second removed item:",removed2)

# Clearing the dictionary
student.clear()

# Printing the final dictionary
print("\nFinal Dictionary:")
print(student)

# Difference between pop() and popitem() :
# pop() removes the key that we give
# popitem() removes the last key-value pair






# update() and pop()
# Creating a dictionary
info = {
  "brand": "Samsung", 
  "model": "A52", 
  "price": 25000
  }

# Updating the dictionary
info.update({
    "color": "Black", 
    "price": 24000})

# Removing the key using pop()
removed = info.pop("model")
print("Removed value :",removed)

# Printing the final dictionary
print(info)





# Nested Dictionary

# Creating a Dictionary
students = { 
    "s1": {"name": "Rahul", "age": 20, "marks": 88}, 
    "s2": {"name": "Sneha", "age": 21, "marks": 95} 
    }

# Printing the details of the first student
print("First Student Details:")
print(students["s1"])

# Printing the marks of the second student
print("\nMarks of Second Student:")
print(students["s2"]["marks"])

# Adding math marks for the first student
students["s1"].update({"math": 90})

# Printing the updated details of the first student
print("\nUpdated First Student Details:")
print(students["s1"])





# Creating a Dictionary

person = {
    "name": "Priya", 
    "age": 21, 
    "profession": "Engineer"
    }

# Using get() to access age
print("Age:",person.get("age"))

# Accessing the non existing key
print("Salary:",person.get("salary"))

# Printing all the keys
print("Keys:")
print(person.keys())

# Printing all the values
print("Values:")
print(person.values())

# Printing all the key value pairs
print("Key value pairs:")
print(person.items())





# Accessing and modifying elements

# Creating a Dictionary
student = { 
    "name": "Tanvi", 
    "age": 21, 
    "city": "Pune", 
    "marks": 88 
    }

# Printing the value of name using quare brackets
print("Name:",student["name"])

# Updating the marks
student.update({"marks":92})

# Adding a new key
student.update({ "Grade": "A"})

# Printing the updated dictionary
print("Updated Dictionary :")
print(student)
 



# Creating Dictionaries

# Empty dictionary using two different ways :
# First way
d1 = {}

# Second way
d2 = dict()

print("Empty dictionary Way 1:", d1)
print("Type:", type(d1))
print("Empty dictionary Way 2:", d2)
print("Type:", type(d2))

# Dictionary with string keys

student = {
    "name": "Tanvi",
    "city": "Pune",
    "course": "AIML"
}

print("\nDictionary with string keys:")
print(student)
print("Type:", type(student))

# Dictionary with integer keys

integers = {
    1: "One",
    2: "Two",
    3: "Three"
}

print("\nDictionary with integer keys:")
print(integers)
print("Type:", type(integers))

# Mixed data type dictionary

mixed = {
    "name": "Tanvi",     # String
    "age": 21,           # Integer
    "marks": 89.5        # Float
}

print("\nMixed data type dictionary:")
print(mixed)
print("Type:", type(mixed))"""

