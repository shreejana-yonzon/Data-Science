#recursive function : self calling function, think about base case, infinite call is denial, it store data in stack which work in FIFO methods.Recursive case is the pattern repeated to access base case.

# sum of natural numbers
# def sum_natural(n):
#     if n == 1:
#         return 1
#     return n + sum_natural(n-1)
# print(sum_natural(20))

#print(sum_natural(10000)) #maximum recursion depth exceeded in comparison == stack overflow

# factorial of nth number
# def fact(n):
#     if n==0 or n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))

#flatten the list using recursive function
# example_list = [1,2,[3,4,[5,6],7],8,9,[10]]
# result_list  = []
 
# def flatten_list(l):
#     for i in l:
#         if isinstance(i, list):
#             flatten_list(i)
#         else:
#             result_list.append(i)
#     return result_list

# num_list = flatten_list(example_list)
# max_value = 0
# for i in num_list:
#     if i > max_value:
#         max_value = i
# print(max_value)


# Higher order function: 
# def parent_function(func):
#     print(func)
#     def child_function():
#         print("My name is ")
#         func()
#         print("I am from Nepal.")
#     return child_function

# @parent_function
# def name():
#     print("Ram")
# name()
# print(name()) # it print none


# def validate_divider(func_add):
#     # print (func_add)
#     def child_function(a,b):
#         if b == 0:
#           return 'cannot be divide by zero'
#         else:
#             return func_add(a,b)
#     return child_function
        

# @validate_divider
# def divide(a,b):
#     return a/bs
# print(divide(10,2))

#create a function that can validate the age of a person 
#if age < 18, return "you are not eligible for voting"
#if age > 18, return "you are eligible for voting"


# def validate_age(func):
#     print(func)
#     def child_function(age):
#         if age < 18:
#             return "you are not eligible for voting"
#         else:
#             return func(age)
#     return child_function

# @validate_age
# def voting_age(age):
#     return "you are eligible for voting"
# print(voting_age(15))
    
#create arithmetic operations function like add, sub, mul and div
# create a higher order function that take two numbers and an operator and return the result



def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b


def calculator(a,b,operator_address):# operator_address which takes address 
    return operator_address(a,b) # it calls the memory address of (a,b) arguments

print(calculator(10,5,add))
print(calculator(18,5,sub))
print(calculator(7,5,mul))
print(calculator(18,3,div))

#create a user with username password and role dict data type
# create a function to check if the user us admin or not
# def is_admin(func):
#     def child_function_admin(user):
#         if not user.get('role'):
#             return 'role must be required.'
#         if user.get('role') != 'admin':
#             return 'You are not authorized to perform this action.'
#         return func(user)
#     return child_function_admin

# @is_admin
# def delete_database(user):
#     print(f'you are authorized. You can delete.')
#     return 'database deleted'

# user = {
#     'username': 'admin',
#     'password': 'password',
#     'role' :'staff'
# }
# print(delete_database(user))


def is_authenticated(func):
    def child_function_admin(user):
        user_container = [{
    'username': 'admin',
    'password': 'password',
    'role' :'staff'},{
    'username': 'admin1',
    'password': 'password1',
    'role' :'staff'}
                     ]
        
        for container_data in user_container:
            if user.get('username') == container_data('username') and user.get('password') == container_data('password'):
                return 'you are authentic user'
            
            
        
    return child_function_admin
    
        
        
    return child_function_admin



@is_authenticated
def migrated_remote_server(user):
    print(f'you are authorized user.')
    return 'server is migrated'

user = {
    'username': 'admin',
    'password': 'password',
    'role' :'staff'
}

print(migrated_remote_server(user))