# String format
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"My name is {name.capitalize()} and I am {age} years old.")

#iterables = loops like while and for

#variable vitra index
name = "Nepal"
print(len(name))
print(id(name))
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# indexError - string index out of range
print(name[5]) 

# Slicing in string: starting index and end index
# variable [start:end:step]
print(name[0:3])
print(name[2:5])
print(name[::]) # default j xa tyahi print garxa
print(name[::2]) # npl
print(name[::-1]) # reversing the string.

# string mutable and immutable : to check this we need to check memory address.
name += ' '
name += 'country'
print(name)
print(id(name))


# To check integers mutable and immutable:
num1 = 65
print( num1)
print(id(num1))

num1 += 10
print(id(num1))

# To check float mutable and immutable:
num1 = 65
print( num1)
print(id(num1))

num1 += 10
print(id(num1))