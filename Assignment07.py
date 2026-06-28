# Taking input from the user
name = input("Enter name: ")
roll = int(input("Enter roll number: "))
mark1 = int(input("Enter mark of Sub1: "))
mark2 = int(input("Enter mark of Sub2: "))
mark3 = int(input("Enter mark of Sub3: "))

# Storing the data in a tuple using packing
student = name, roll, mark1, mark2, mark3

# Printing the complete record
print("\nStudent Record:", student)

# Unpacking the tuple
name, roll, mark1, mark2, mark3 = student

# Printing values with labels
print("\nStudent Details")
print("Name:", name)
print("Roll Number:", roll)
print("Marks of Sub1:", mark1)
print("Mark of Sub2:", mark2)
print("Mark of Sub3:", mark3)

# Taking a mark from the user to count
mark = int(input("\nEnter a mark to count: "))
print("This mark appears", student.count(mark), "time(s)")

# Creating a nested tuple for multiple students
student1 = ("Akshada", 45, 85, 90, 88)
student2 = ("Tanuja", 51, 78, 82, 80)

records = (student1, student2)

# Printing all student records
print("\nAll Records:", records)

# Accessing specific values
print("First student's name:", records[0][0])
print("Second student's roll number:", records[1][1])













































"""# Creating a tuple
coordinates = (10, 20)

print("Original tuple:", coordinates)

# Trying to change the first element
# coordinates[0] = 15
# Error: Tuples are immutable so their values cannot be changed

# Trying to add a new element
# coordinates.append(30)
# Error: Tuples does not support append() method

# Converting tuple to list to modify it
coord_list = list(coordinates)

# Making changes in the list
coord_list[0] = 15
coord_list.append(30)

# Converting list back to tuple
coordinates = tuple(coord_list)

print("Modified tuple:", coordinates)





# Create a tuple of fruits
fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

# Finding first index of banana
print("First index of banana:", fruits.index('banana'))

# Finding banana from index 2
print("Banana from index 2:", fruits.index('banana', 2))

# Finding kiwi using try-except
try:
    print("Index of kiwi:", fruits.index('kiwi'))
except :
    print("Kiwi not found")




    
    
# Create a tuple of grades
grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

# Counting how many times A appears
print("A appears", grades.count('A'), "times")

# Counting how many times B appears
print("B appears", grades.count('B'), "times")

# Taking a grade from the user
grade = input("Enter a grade: ")

# Printing how many times the grade appears
print(grade, "appears", grades.count(grade), "times")





# Creating a tuple 
student = ('Rahul', 20, 'Computer Science', 'A')

# Iterating through the tuple using a for loop
print("Items in the tuple:")
for element in student:
    print(element)

# Unpacking the tuple into variables
name, age, branch, grade = student

# Printing the values 
print("\nUnpacked Elements :")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("Grade:", grade)





# Creating a nested tuple to represent a 3 x 3 matrix
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Printing the first row
print("First row:", matrix[0])

# Printing the element at second row and third column
print("Element at second row and third column:", matrix[1][2])

# Printing the element at third row and first column
print("Element at third row and first column:", matrix[2][0])





# Creating a tuple
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Elements from index 2 to 7
print("Index 2 to 7:", numbers[2:8])

# First 5 elements
print("First 5 elements:", numbers[:5])

# Last 4 elements
print("Last 4 elements:", numbers[-4:])

# Every second element
print("Every second element:", numbers[0:11:2])

# Entire tuple in reverse order
print("Reverse order:", numbers[::-1])

# Slicing syntax - [start:end:step]
# start = where slicing begins
# end = where slicing stops
# step = how many positions to jump





# Create a tuple 
colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

# Printing elements using indexing
print("First element:", colors[0])
print("Third element:", colors[2])

# Printing elements using negative indexing
print("Last element:", colors[-1])
print("Second last element:", colors[-2])

# Taking index number from the user
index = int(input("Enter an index number: "))

# Printing the element 
print("Element at index", index, "is", colors[index])




# Tuple packing 
# Tuple without using parentheses
student = "Tanvi", 21, "Pune"

# Print the tuple and its type
print("Tuple:", student)
print("Type:", type(student))

# Unpacking the tuple into separate variables
name, age, city = student

# Print each value separately
print("Name:", name)
print("Age:", age)
print("City:", city)





# Program to create different types of tuples

# Tuple with 5 numbers using parentheses
nums = (10, 20, 30, 40, 50)

# Mixed tuple containing different data types
mixed = (25, "Tanvi", 5.5, True)

# Empty tuple using two different ways
empty1 = ()
empty2 = tuple()

# Single element tuple
single = (50,)

# Rules for single element tuples :
# A single element tuple must have a comma after the value
# Without the comma, Python does not consider it a tuple

# Printing all tuples with their types
print("Tuple with 5 numbers:", nums)
print("Type:", type(nums))

print("\nMixed tuple:", mixed)
print("Type:", type(mixed))

print("\nEmpty tuple 1:", empty1)
print("Type:", type(empty1))

print("\nEmpty tuple 2:", empty2)
print("Type:", type(empty2))

print("\nSingle element tuple:", single)
print("Type:", type(single))"""                                                      