#traditional method 
#read a file
# file = open('text.txt','r')
# print(type(file))
# print(file.read()) #it read a file from buffer memory i.e temporary memory
# file.close()


#write a file
# file = open('text.txt','w')
# file.write('Hello, best wishes for DSML course.')
# file.close()

#append file
# file = open('text.txt','a')
# file.write('\n classes are open in next wednesday.')
# file.close()



#Modern Method:
#with statement : with is a context manager
# with open('text.txt','r') as file:
#     print(file.read())

# with open('text.txt','w') as file:
#file.write('hi, stay clam and focused.')

# with open('text.txt','a') as file:
#     file.write('\n Have good day.')

# with open('data.txt','r') as file:
#     print(file.read())


# try:
#     file = open('text.txt', 'r')
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print('No such file or directory.')
# except FileExistsError: #already exist file 
#     print('File already exists.')
# finally:
#     print('File closed.')
    
    
#to create a new file 
# file = open('data.txt','x')
# file.write('Welcome to DSML class.')
# file.close()

#count the number of words in file
# with open('text.txt','r') as file:
    # print(type(file.read())) #file exhausted data type hunxa onces a life is read is disappear(exhausted)
    # print(type(len(file.read().split()))) #int
    # print(type(file.read().split())) #List

#calculate the number of lines in file
# with open('text.txt','r') as file:
#     print(len(file.readline()))   

# check if 'python' word in present in file

# check if 'python' word is present in file

# with open('text.txt', 'r') as file:
#     result = file.read()
    
#     if 'python' in result:
#         print('word "python" is in the file.')
#     else:
#         print('word "python" is not in the file.')

#create a function to take the user input password and
#check the existence of password in files as a word

def passwordChecker():
    try:
        password = input('Enter a password: ')
        
        with open('text.txt', 'r') as file:
            check_password = file.read().split()
            
            if password in check_password:
                print('Password is found!')
            else:
                print('Password is not found!')
                
    except FileNotFoundError:
        print('file not found.')
    
    finally:
        print('final block is executed.')

passwordChecker()