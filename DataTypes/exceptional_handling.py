#exceptional handling in python
# try-except block
# try-except-else block
# try-except-else-finally block

#simple example of try and except block
# try:
#     a = int(input('enter a number'))
#     b = int(input('enter a number'))
#     print(a/b)
# except ZeroDivisionError:
#     print('Cannot be divide by zero.')
# except ValueError:
#     print('Invalid input')


# create a function that takes two numbers as input and return their sum
#use try-except block to handle the case where the input is not a number
# Create a function that takes two numbers as input and return their sum
# Use try-except block to handle the case where the input is not a number

# def sum():
#     try:
#         a = int(input('Enter a number: '))
#         b = int(input('Enter a number: '))
#         print (a + b)
    
#     except ValueError:
#         print("Invalid input")

# print(sum())


#try-except-else Block
# try:
#     a = int(input('enter a number'))
#     b = int(input('enter a number'))
#     print(a/b)
# except ZeroDivisionError:
#     print('Cannot be divide by zero.')
    
# except ValueError:
#     print('Invalid input')
    
# else:
#     print('No error occurred.')


#try-except-else-finally Block
# try:
#     a = int(input('enter a number'))
#     b = int(input('enter a number'))
#     print(a/b)
# except ZeroDivisionError:
#     print('Cannot be divide by zero.')
    
# except ValueError:
#     print('Invalid input')
    
# else:
#     print('No error occurred.')
    
# finally:
#     print('finally block executed.')
    
#create a function that takes any kind of iteration as input
#and try to reverse it
#use try-except-else-finally block to handle the case where the input is not an iterable

def reverse_iteration(data):
    error_type = None
    try:
       result = data[::-1]
       print(result)
    except TypeError:
        error_type = 'TypeError'
        message = 'Invalid input'
    else:
        print('reverse successfully!')
    finally:
        if error_type:
            print( f'{error_type} {message}')
        else:
            print (result)
            
reverse_iteration()
