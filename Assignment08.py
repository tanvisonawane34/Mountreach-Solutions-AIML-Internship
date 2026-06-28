# Creating an empty set
items = set()

# Menu starts
while True:

    print("\n----- MENU -----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show All Unique Items")
    print("4. Check if an Item Exists")
    print("5. Clear All Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add a new item
    if choice == 1:
        item = input("Enter an item: ")
        items.add(item)
        print("Item added.")

    # Remove an item
    elif choice == 2:
        item = input("Enter item to remove: ")
        items.discard(item)
        print("Item removed if it was present.")

    # Display all unique items
    elif choice == 3:
        print("Unique Items:", items)

    # Check whether an item is present
    elif choice == 4:
        item = input("Enter item to check: ")

        if item in items:
            print("Item is present.")
        else:
            print("Item is not present.")

    # Remove all items
    elif choice == 5:
        items.clear()
        print("All items have been cleared.")

    # Exit the program
    elif choice == 6:
        print("Thank you!")
        break

    # If the user enters a wrong choice
    else:
        print("Invalid choice. Please try again.")

# Sets store only unique items
# Duplicate items are ignored automatically
























































"""# List of student scores
scores = [85, 92, 78, 92, 85, 88, 95, 78]

print("Original scores:", scores)

# Converting the list to a set
unique_scores = set(scores)
print("\nUnique scores:", unique_scores)

# Converting the set back to a sorted list
sorted_scores = sorted(unique_scores)
print("Sorted unique scores:", sorted_scores)

# Printing the total number of unique scores
print("Total unique scores:", len(unique_scores))

# set() - removes duplicate values
# sorted() - arranges the scores in ascending order







# Creating an empty set
numbers = set()

# Taking 6 numbers from the user
numbers.add(int(input("Enter first number: ")))
numbers.add(int(input("Enter second number: ")))
numbers.add(int(input("Enter third number: ")))
numbers.add(int(input("Enter fourth number: ")))
numbers.add(int(input("Enter fifth number: ")))
numbers.add(int(input("Enter sixth number: ")))

print("\nSet after taking input:", numbers)

# Adding two more numbers
num1 = int(input("Enter one more number to add: "))
numbers.add(num1)

num2 = int(input("Enter another number to add: "))
numbers.add(num2)

# Removing one number using discard()
remove = int(input("Enter a number to remove: "))
numbers.discard(remove)

# Printing the final set
print("\nFinal set:", numbers)

# Printing the length of the set
print("Total elements in the set:", len(numbers))






# Creating two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union using union() method
print("\nUnion using union():", A.union(B))

# Union using | operator
print("Union using | :", A | B)

# Union gives all elements from both sets
# Duplicate values are included only once

# Intersection using intersection() method
print("\nIntersection using intersection():", A.intersection(B))

# Intersection using & operator
print("Intersection using & :", A & B)

# Intersection gives only the common elements present in both sets





# Creating two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

# Making a copy of set1
copy1 = set1.copy()

# Updating set1 with set2
set1.update(set2)

# Printing the results
print("\nCopy of Set 1:", copy1)
print("Updated Set 1:", set1)

# copy() - creates another set with same elements
# update() - adds all elements from one set to another
# Duplicate values are added only once 






# Creating a set
s = {100, 200, 300, 400, 500}

print("Original set:", s)

# Removing one element using pop()
removed = s.pop()
print("\nRemoved element:", removed)

# Printing the set after pop()
print("Set after pop():", s)

# Clearing the entire set
s.clear()

# Printing the empty set
print("\nSet after clear():", s)

# remove() - removes the given element
# It gives an error if the element is not present in the set

# discard() - also removes the given element
# It does not give an error if the element is not present

# pop() - removes any one random element from the set
# We cannot choose which element will be removed





# Create a set
fruits = {"apple", "banana", "mango"}

print("Original set:", fruits)

# Adding 'orange'
fruits.add("orange")
print("\nAfter adding orange:", fruits)

# b) Adding 'banana' again
fruits.add("banana")
print("\nAfter adding banana again:", fruits)

# c) Removing 'mango'
fruits.remove("mango")
print("\nAfter removing mango:", fruits)

# d) Removing 'grape' using discard()
fruits.discard("grape")
print("\nAfter discarding grape:", fruits)

# discard() does not give an error if the element is not present
# remove() gives an error in such cases





# Membership Testing

# Take 5 colors as input from the user
colors = set()

colors.add(input("Enter first color: "))
colors.add(input("Enter second color: "))
colors.add(input("Enter third color: "))
colors.add(input("Enter fourth color: "))
colors.add(input("Enter fifth color: "))

# Display the set
print("\nColors in the set:", colors)

# Asking the user to enter a color to search
search_color = input("Enter a color to check: ")

# Checking membership using 'in'
if search_color in colors:
    print(search_color, "is present in the set")

# Checking membership using 'not in'
if search_color not in colors:
    print(search_color, "is not present in the set")




    
    
# Characteristics of Sets

# Creating a set with duplicate values
numbers = {10, 20, 30, 20, 40, 10, 50}

# Printing the set
print("Set:", numbers)

# Duplicate values 10 and 20 will removed automatically
# So each value appears only once in the output

# Printing the set multiple times
print("\nPrinting the set again:")
print(numbers)

print("\nPrinting the set one more time:")
print(numbers)

# Sets are unordered, so the order of elements is not fixed
# The order may look different on different computers

# Trying to access the first element using indexing

# print(numbers[0])

# This gives an error because:
# TypeError: 'set' object is not subscriptable
# because sets do not support indexing







# Creating Different Types of Sets

# Set with 5 integers
numbers = {10, 20, 30, 40, 50}
print("Set of integers:", numbers)
print("Type:", type(numbers))

# Set with mixed data types
mixed_set = {21, "Tanvi", 7.5}
print("\nMixed set:", mixed_set)
print("Type:", type(mixed_set))

# Creating an empty set
empty_set = set()      
print("\nEmpty set:", empty_set)
print("Type:", type(empty_set))

# Creating a set from the string 
string = set("hello")
print("\nSet from string 'hello':", string)
print("Type:", type(string))

# Sets automatically remove duplicate values
# In the word "hello", the letter 'l' appears twice
# but the set stores it only once"""                             