#convert string to uppercase and lowercase
a = 'Environment'
print("Uppercase of a string",a.upper())
print("Lowercase of a string",a.lower())

#Reverse a string
# reversed_string = "".join(reversed(a))
# print("The reversed of string a is:",reversed_string)
#From slicing method
# print("The reverse string of a is:", a[::-1])


#Count number of characters
# print("To count of characters of a is:", len(a))

#check if a string is a palindrome
# b = input("Enter any string at here:")
# if b == b[::-1]:
#     print(f"A string {b} is palindrome.")
# else:
#     print(f"A string {b} is not palindrome.")


#count vowels in a string

vowels = 'aeiou'
count = 0

for char in a.lower(): #go through each letter
    if char in vowels: # check is it in a vowels
        count += 1     # if yes -> count it
print(f"Vowels count of {a} is",count)


# Replace spaces with underscores
original_string= input("Enter your message:")
print("The original string is: ", original_string)

replace_string = original_string.replace(' ','_')
print("The replaced string is: ",replace_string)
