#Create a variables of different data types(int,float,string,boolean)
#print their types using type()

a = 6
b = 6.78
c = 'Hello'
d = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#perform arithmetic operations(addition, subtraction, multiplication, division)
# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))

# print("Addition of two numbers: ", num1 + num2)
# print("Subtraction of two numbers: ", num1 - num2)
# print("Multiplication of two numbers: ", num1 * num2)
# if num1 == 0:
#     print("zero cannot be divided.")
# else:
#     print(f"Division of {num1} by {num2} is : ", num1/num2 )

#swap two numbers without using a third variable
a = 15
b = 20

print("Before swapping value of a: ", a)
print("Before swapping value of b: ", b)

a,b = b,a    # Called tuple packing and unpacking method.

print("After swapping value of a:", a)
print("After swapping value of b:", b)



#convert a string into an integer
a = '131235'
print(type(a)) # a is string

a = int(a) # a is converted into integer.
print(type(a)) # a is integer.

#find square and cube of a number
a = int(input("Enter your number: "))
square = a**2
cube = pow(a,3)
print(f"The square of {a} is:", square)
print(f"The cube of {a} is:", cube)
