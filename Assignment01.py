"""name = "Tanvi Somnath Sonawane"
age = 20
height = 1.60
student = True

print("Name :",name)
print("Age :",age)
print("Height :",height)
print("Student :",student)

print(type(name))
print(type(age))
print(type(height))
print(type(student))

 #I use simple variable names because they are simple to understand


a = "Hello"
b = 10
c= 5.5
d = False

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

print("Integer converted to float:",float(b))
print("Float conerted to integer:",int(c))


a = 15
b = 4

print("Addition:", a+b)
print("Substraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus:", a%b)
print("Power:", a**b)

# / gives the exact division result including decimal values
# // gives the answer as a whole number and removes the decimal part



x = 25
y = 30
z = 25

print("Is x is greater than y? :", x > y)
print("Is x equal to z? :",x == z)
print("Is x less than or equal to y and y not equal to z? :",(x<=y)and(y!=z))
print("Is x greater than y or x equal to z? :",(x>y)or(x==z))



name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

print("Name:", name)
print("Age:", age)



height = float(input("Enter your height:"))
weight = int(input("Enter your weight:"))
bmi = weight / (height**2)
print("BMI =", round(bmi,2))


#This program calculates the area and perimeter of a rectangle

#Taking length and width from user
length = int(input("Enter length:"))
width = int(input("Enter width:"))

#Area tells us the space inside the rectangle
area = length*width
#Perimeter tells us the local boundary length
perimeter = 2*length+width

#Printing the results
print("Area of a rectangle:",area)
print("Perimeter of a rectangle:",perimeter)



fruits = ["mango","apple","banana","cherry"]
score = 50

score += 25
print("Updates score:",score)
print("Is apple in the fruits list?:","apple"in fruits)
print("Is grape not in the fruits list?:","grape"not in fruits)


#This program displays the student information

#Taking input from user
name = str(input("Enter a name:"))
age = int(input("Enter your age:"))
city = str(input("Enter city:"))

python = float(input("Enter marks in python: "))
math = float(input("Enter marks in mathematics:"))
java = float(input("Enter marks in java:"))

#calculating the total marks
total = python + math + java

#calculating the total percentage
percentage = total /3

#Displaying Student information
print("Name:",name)
print("Age:",age)
print("City:",city)
print("Marks in python:",python)
print("Marks in maths:",math)
print("Marks in java:",java)
print("total marks:",total)
print("Percentage:",percentage)"""


#name should be stored in a string
name = "Alice"
age = 20
#city name should be inside double quotes
city = "Amsterdam"

print("My name is",name)
#age is a number so comma is used
print("I am",age,"years old")
print("I live in",city)

#checking if age is greater than 18
print("Adult:",age > 18)



