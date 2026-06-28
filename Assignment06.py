# Create an empty list
marks = []

# Taking marks from the user using for loop
for i in range(5):
    mark = int(input("Enter subject mark: "))
    marks.append(mark)

# Printing the list
print("Marks list:", marks)

# Adding one more mark
extra_mark = int(input("Enter one more subject mark: "))
marks.append(extra_mark)

print("Updated marks list:", marks)

# Finding highest and lowest marks
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))

# Sorting marks in descending order
marks.sort(reverse=True)
print("Marks in descending order:", marks)

# Calculating average
average = sum(marks) / len(marks)
print("Average marks:", average)

# Total number of subjects
print("Total subjects:", len(marks))





































"""# Create two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using extend()
list1.extend(list2)
print("Using extend():", list1)

# Creating a copy of list1 again
list1 = [1, 2, 3]

# Using append()
list1.append(list2)
print("Using append():", list1)

# Difference between extend() and append():
# extend() - adds each element of the second list
# append() - adds the whole list as a single element  





# Create a list of marks
marks = [45, 78, 65, 90, 34, 82, 71]

# Sort the list in ascending order
marks.sort()
print("Ascending order:", marks)

# Sort the list in descending order
marks.sort(reverse=True)
print("Descending order:", marks)

# Creating the original list again
marks = [45, 78, 65, 90, 34, 82, 71]

# Reverse the original list
marks.reverse()
print("Reversed list:", marks)

# Difference between sort() and reverse():
# sort() - Arranges the elements in order
# reverse() - Only changes the direction of the list





# index() and count()

scores = [85, 92, 78, 92, 65, 92, 88]

# Finding the index of the first occurrence of 92
print("Index of 92:", scores.index(92))

# Counting how many times 92 appears
print("Count of 92:", scores.count(92))

# Taking a number from the user
num = int(input("Enter a number: "))

# Checking if the number exists in the list
if num in scores:
    print("Index:", scores.index(num))
    print("Count:", scores.count(num))
else:
    print("Number not found in the list")




# Create a list
items = [10, 20, 30, 20, 40, 50]

# Removing the first occurrence of 20
items.remove(20)
print("After removing first occurence of 20:", items)

# Removing the item at index 3
removed_item = items.pop(3)
print("Removed value:", removed_item)
print("After pop(3):", items)

# Removing the last item
items.pop()
print("After removing last item:", items)

# Clearing the entire list
items.clear()
print("After clear():", items)

# Difference between remove() and pop():
# remove() - removes an item by its value
# pop() -  removes an item by its index and returns the removed value 





# Create an empty list
cities = []

# Take input from the user
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

# Add cities using append() function
cities.append(city1)
cities.append(city2)
cities.append("Delhi")
cities.append("Mumbai")
cities.append("Chennai")

# Adding a city at position 2
cities.insert(2, "Pune")

# Printing the final list
print("Final list of cities:", cities)





# Modifying Lists
# Creating a list
colors = ["red", "blue", "green", "yellow"]

# Changing "blue" to "purple"
colors[1] = "purple"
print("Updated list:", colors)

# Changing the last item to "black"
colors[-1] = "black"
print("Final list:", colors)





# Slicing syntax: list[start : stop : step]
# start = where slicing begins
# stop = where slicing ends
# step = how many positions to move each time

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# First 4 elements
print("First 4 elements:", numbers[0:4])

# Last 3 elements
print("Last 3 elements:", numbers[-3:])

# Elements from index 2 to 7
print("Elements from index 2 to 7:", numbers[2:8])

# Every second element
print("Every second element:", numbers[::2])

# Reverse the list
print("List in reverse order:", numbers[::-1])




# Indexing and Negative Indexing
fruits = ["apple", "banana", "mango", "orange", "grape"]

# Printing values using positive indexing
print("First Item :",fruits[0])
# To print third item
print("Third Item :",fruits[2])

# Printing values using negative indexing
print("Last Item :",fruits[-1])
# To print second last item
print("Secind Last Item :",fruits[-2])


# Taking an index from the user
index = int(input("Enter an index number: "))

# Printing the item at that index
print("Item at index", index, "is:", fruits[index])






# Creating Lists

# List of 5 integers directly
nums = [50,60,70,80,90]

# Empty list using two different methods
empty_lst = []              # Using square brackets
empty_lst2 = ()             # Using list() function

# A List containing different data types
a = ["Tanvi", 21 ,5.3, True]

# A List of 7 zeros using repetition 
x = [0]*7

# Printing all lists with labels
print("List of 5 integers:", nums)
print("Empty list using []:", empty_lst)
print("Empty list using list():", empty_lst2)
print("Mixed data type list:",a)
print("List of 7 zeros:", x)"""


