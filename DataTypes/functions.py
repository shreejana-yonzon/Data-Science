#function: reusability and readability. it helps in redurant task.

#Higher-order function: it takes function as argument and also return function. no return value is none

# def add(a,b):
#     print( a+b )

# #function calling
# result = add(2,3)
# print(result) 

# def sub(a,b):
#     return (a-b)

# result = sub(3,1)
# print(result)

#print(sub) # it print location of sub function.
# def mul(a,b):
#     return (a*b)

# result = mul(3,8)
# print(result)


# def div(a,b):
#     if b == 0:
#         return 'cannot divide by zero'
#     return (a/b)

# result = div(16,7)
# print(result)

# Find max number 
# def find_max(a=10,b=60,c=90):
#     print(a,b,c)
#     if a > b and a > c:
#        return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
    

# function calling
# result = find_max(5,10,3)
# print(f'The greatest value is {result}')
#print(find_max(b=10,a=30,c=70)) # positional arguments doesn't effect
#print(find_max(10,a=30,c=70)) # mix arguments
#print(find_max(10,30,70)) # default value can be override

#arbitrary argument
# def find_max(**kwargs):
    
#     name = kwargs.get('name')
#     age = kwargs.get('age')
#     print(name,age)
  
# print(find_max(name = 'nepal', age = 20)) 


#Getting by keys
# def check_key(key, **kwargs):
#     print(key)
#     check = kwargs.get(key)
#     if check:
#         return 'key exist'
#     else:
#         return 'key does not exist'
    
   
# print(check_key('name',name = 'nepal', age = 20)) 

#Accessing by Values
# def check_values(value, **kwargs):
#     print(value)
#     check = kwargs.get(value)
#     if check:
#         return 'value exist'
#     else:
#         return 'value does not exist'
    
   
# print(check_values('nepal',name = 'nepal', age = 20)) 

#Addition of three :
# def sum_number(**kwargs):
#     total = 0
#     for value in kwargs.values():
#         total += value
#     return total

# result = sum_number(a=40,b=30,c=60,d=100)
# print(f'The total sum is {result}')


# Nested loops:

# for i in range(5):
#     for j in range(5):
#         print(i,j)

#classwork nested for loop
#find the sum of all the value in nested for loop
# sum = 0
# for i in range(5):
#     for j in range(5):
#         sum += i + j
#         print(sum)

#Nested function to greet:state management or state retention, function ko return value function nai huna sakxa. 

# def greet(name):
#     def get_message(name):
        

#State retention function:
# def parent_counter():
#     count = 0
#     def child_counter():
#         nonlocal count
#         count += 1
#         return count
#     return child_counter
# counter = parent_counter()
# print(counter())
# print(counter())
# print(counter())
  


#find the max value from a list of parent scope and pop the max value from the list until the list is empty
# def parent_list():
#     my_list = [1, 2, 3, 4, 5]
    
#     def child_list():
#         nonlocal my_list
#         max_val = max(my_list)
#         my_list.remove(max_val)
#         print(max_val)
    
#     return child_list

#create discount_parent function with nested child function of apply_discount  and set_discount

# def discount_parent():
#     current_discount = 0.1
    
#     def apply_discount(price):
#         nonlocal current_discount
#         price = price * (1-current_discount)
#         return price
#     def set_discount(discount_price):
#         nonlocal current_discount
#         current_discount = discount_price
#     return apply_discount, set_discount

# apply_discount, set_discount = discount_parent()
# print(apply_discount(100))
# set_discount(0.2)
# print(apply_discount(100))

#recursive function : self calling function, think about base case, infinite call is denial, it store data in stack which work in FIFO methods.Recursive case is the pattern repeated to access base case.

 


