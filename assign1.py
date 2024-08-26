
ASSIGN NUMBER 1
Q1)
a = 3.0
b = 6.6
print(a+b)
print(a*b)
print(a**b)
print(a/b)
print(a%b)

print(a>b) 

Q2)Write a python program to Accept Student Name,
Roll Number and Marks of the 3
subjects from the user. Calculate the percentage 
of the marks and display it. Display
the Subject with Highest and lowest marks.
name = input("Student name: ")
roll = int(input("Student Roll nos: "))
mark1 = float(input("Mark of first sub: "))
mark2 = float(input("Mark of second sub: "))
mark3 = float(input("Mark of third sub: "))

percentage = (mark1 + mark2 + mark3) / 300 * 100
print("Percentage are ",percentage,"%")

highest_mark = max(mark1, mark2, mark3)
lowest_mark = min(mark1, mark2, mark3)

print("Highest marks are: ",highest_mark)
print("LOwest marks are: ",lowest_mark)
Q3)Write a python program to accept an integer number 
form the user and display is it an
even number or odd number.


num = int(input('Enter an integer number: '))

if(num%2==0):
    print("EVEN NUM")
else:
    print("ODD NUM")

Q4)Write a python program to accept 5 numbers 
from the user and display their cube
values.

# Accept input from the user
print("Enter five numbers:")
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())

# Calculate the cube of each number
cube1 = num1 ** 3
cube2 = num2 ** 3
cube3 = num3 ** 3
cube4 = num4 ** 3
cube5 = num5 ** 3

# Display the cube values
print(f"The cube of {num1} is {cube1}")
print(f"The cube of {num2} is {cube2}")
print(f"The cube of {num3} is {cube3}")
print(f"The cube of {num4} is {cube4}")
print(f"The cube of {num5} is {cube5}")
