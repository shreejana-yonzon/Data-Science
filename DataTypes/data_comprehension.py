listing = [i for i in range(5)]
[0] #first element
[0,1] #second element
[0,1,2] #third element
[0,1,2,3] #forth element
[0,1,2,3,4] #second element
print(listing)

#create a list of even number less than or equal to 10

result_list = [i for i in range(11) if i % 2 == 0]
print(result_list)

#general structure of data comprehension
# [expression iteration condition]

#create a list of odd number less than or equal to 10
odd_list = [i for i in range(11) if i % 2 != 0]
print(odd_list)

#list containing the names
name_list = ['Ashish', 'Ajay', 'Aayush']
#create a list of names starting with A
#create a new list containing name that start with A

name_list = [i for i in name_list if i.startswith('A') and i.endswith('h')]
print(name_list)


#dictionary comprehension
#general structure of dict comprehension
# {key:value for item in iteration condition}

sqr_dict = {i:i*i for i in range(5)}
print(sqr_dict)

#create a dict from string "Hello world"
# the key should be the character and the value should be the count of character
#the string is "hello world"

str_dict = "Hello world"
result_dict = {i : str_dict.count(i) for i in str_dict  if i != ' ' }
print(result_dict)

#create a dict from list of strings
#the key should be the string and the value should be the length of the string
#the list is ['hello','world','python','java']

string_list = ['hello','world','python','java']
res_list = {i : len(i) for i in string_list}
print(res_list)


#set comprehension
#general structure of set comprehension
# {expression for item in iterable condition}

#create a set from list containing the natural numbers less than 100
#take only prime number and store in a set
# Create a set from natural numbers less than 100
# Take only prime numbers and store in a set

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(2, n): 
        if n % i == 0:
            return False
    return True

prime_numbers = {i for i in range(1, 100)  if is_prime(i)}
print(prime_numbers)



