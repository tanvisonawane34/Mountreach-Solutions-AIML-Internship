# String Analyzer Program

# Ask user to enter a string
str = input("Enter a string: ")

# Print the length of the string
print("Length of the string:", len(str))

# Find the middle position of the string
middle = len(str) // 2

# Print the first half of the string
print("First half:", str[:middle])

# Print the second half of the string
print("Second half:", str[middle:])

# Check if the word "python" is present
if "python" in str.lower():
    print("The word 'python' is present.")
else:
    print("The word 'python' is not present.")

# Print all characters with positive and negative indexes
print("Characters with positive and negative indexes:")

for i in range(len(str)):
    print("Positive Index:", i,
          "| Character:", str[i],
          "| Negative Index:", i - len(str))

# Print the string in reverse
print("Reverse string:", str[::-1])

































"""# Print first 10 even numbers from 2 to 20
print("First 10 even numbers:")

for i in range(2, 21, 2):
    print(i)

# Print numbers from 1 to 30 in steps of 3
print("Numbers from 1 to 30 in steps of 3:")

for i in range(1, 31, 3):
    print(i)

# String slicing
s = "PythonProgramming"

# Print Python
print("First part:", s[0:6])

# Print Programming
print("Second part:", s[6:17])

# Print the string in reverse
print("Reverse string:", s[::-1])





# Ask user to enter a number
num = int(input("Enter a number: "))

# Check if the number is present in range 1 to 50
if num in range(1, 51):
    print("The number is present in range(1, 51)")
else:
    print("The number is not present in range(1, 51)")

# Check if the number is present in range 10 to 100 in step of 5
if num in range(10, 100, 5):
    print("The number is present in range(10, 100, 5)")
else:
    print("The number is not present in range(10, 100, 5)")



    
    
# Ask user to enter a string
s = input("Enter a string: ")

# Print each character with its index
print("Characters with their indexes:")

for i in range(len(s)):
    print(i, s[i])
print()

# Print the string in reverse order
print("String in reverse order:")

for i in range(len(s)-1, -1, -1):
    print(s[i], end="")





# Print numbers from 20 down to 10
print("Numbers from 20 down to 10:")

# Start from 20, stop before 9, decrease by 1
for i in range(20, 9, -1):
    print(i)

# Print numbers from 15 down to 1 in steps of 2
print("Numbers from 15 down to 1 in steps of 2:")

# Start from 15, stop before 0, decrease by 2
for i in range(15, 0, -2):
    print(i)





# range(stop)
# Used when we want to start from 0

# range(start, stop)
# Used when we want to start from a specific number

# range(start, stop, step)
# Used when we want to skip numbers while printing

# Print numbers from 0 to 10
print("Numbers from 0 to 10:")
for i in range(11):
    print(i)
print()
# Print numbers from 5 to 15
print("Numbers from 5 to 15:")
for i in range(5, 16):
    print(i)
print()
# Print odd numbers from 1 to 21
print("Odd numbers from 1 to 21:")
for i in range(1, 22, 2):
    print(i)




    
# Ask user to enter a string
s = input("Enter a string : ")

# To print the length of the string
print("Length of the string :", len(s))

# To print the Last character 
print("Last character :", s[- 1])

# Check if the length is odd
if len(s) % 2 != 0:
    print("Middle character :", s[len(s) // 2])

# Common mistakes with len():
# Using s[len(s)] causes IndexError because indexing starts from 0
# The last character is at index len(s) - 1
# len() gives the number of characters, not the last index                                       






# Ask the user to enter a main string
main = input("Enter the main string :")
# Ask the user to enter a substring
sub = input("Enter the substring :")

# Checking if substring is present
if sub in main :
    print("Substring found!")
else :
    print("Substring not found")

# Checking using not in operator
if sub not in main :
    print("Substring is not present in the main string")






# String Slicing

# Ask user to enter a string
s = input("Enter a String :")

# First 5 characters
print("First 5 Characters :",s[0:5])
# Last 4 characters
print("Last 4 Characters :",s[-4:])
# String in reverse order
print("String in reverse order :",s[::-1])
# Every 2nd character
print("Every 2nd Character of a string :",s[0:11:2])

# start = starting index
# end = ending index (not included)
# step = number of positions to move





# String Indexing 
s = input("Enter a string :")

# To print the first character
print("First Character :",s[0])

# To print the last character
print("Last Character :",s[-1])

# To print the third character from the start 
print("3rd character from the start :",s[2])

# To print the second character from the end
print("2nd character from the end :",s[-2])

# Positive Indexing starts from 0 and moves left to right
# Negative Indexing starts from -1 and moves from right to left"""


