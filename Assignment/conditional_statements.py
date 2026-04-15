#Check if a number is even or odd
# num = int(input("Enter your number:"))

# if num%2 == 0:
#     print(f"The number {num} is even.")
# else:
#     print(f"The number {num} is odd.")
     

#Find the greatest of three numbers
# a = int(input("Enter your first number:"))
# b = int(input("Enter your second number:"))
# c = int(input("Enter your third number:"))

# if a > b and a > c:
#     print(f"The number {a} is greatest.") 
# elif b > a and b >c:
#     print(f"The number {b} is greatest.") 
# else:
#     print(f"The number {c} is greatest.") 


# Check if a number is positive, negative or zero
# if num > 0:
#     print(f"A number {num} is positive number.")
# elif num < 0:
#     print(f"A number {num} is negative number.")
# else:
#     print(f"A number {num} is zero")

#Build a simple calculator using if-else
# num1 = int(input("Enter your first number:"))
# num2 = int(input("Enter your second number:"))
# operation = input("Enter your operator (+,-,*, or /): ")

# if operation == '+':
#     sum = num1 + num2
#     print(f"The sum of {num1} and {num2} is:", sum)
# elif operation == '-':
#     differences = num1 - num2
#     print(f"The differences of {num1} and {num2} is", differences)
# elif operation == '*':
#     product = num1 * num2
#     print(f"The product of {num1} and {num2} is", product)
# elif operation == '/':
#     if num1 == 0:
#         print("It cannot be divided")
#     else:
#         div = num1/num2
#         print(f"The division of {num1} by {num2} is", div)
# else:
#     print("Invalid Operators")

#create a grading system based on marks  
marks = int(input("Enter your mark:"))

if marks >= 90:
    print("Outstanding! You have achieve A+")
elif marks >= 80:
    print("Excellent! You have achieve A")
elif marks >= 70:
    print("Very Good! You have achieve B+")
elif marks >= 60:
    print("Good! You have achieve B")
elif marks >= 50:
    print("Above avg! You have achieve C+")
elif marks >= 40:
    print("Below avg! You have achieve C")
elif marks >=30:
    print("Not Graded")
else:
    print("Better luck next time!!")
    