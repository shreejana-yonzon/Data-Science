#print numbers from 1 to 100
#starting from 1 and goes upto 100 where 101 is excluded.
# for i in range(1,101):
#     print(i)
   
#print even numbers
# print('The even numbers from 1 t0 100 are:')
# for i in range(1,101):
#     if i%2 == 0:
#         print(i)
        
#Generate multiplication table
# num = int(input("Enter your number: "))
# print(f'The multiplication table of {num} is:')
# for i in range(1,11):
#     print(f'{num} * {i} = ',num*i)
    
#find sum of first N numbers
# num = int(input("Enter a number:"))
# sum = 0

# print("The sum of first N numbers:")

# for i in range(1, num+1):
#     sum += i
#     print(sum)
    
#calculate factorial 
# num = int(input("Enter a number to calculate factorial:"))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i
# print('The factorial of {num} is', fact)


#Generate Fibonacci series
num = int(input("Enter a number to find fibonacci series:"))

a,b =0,1
total_fibonacci = 0

for i in range(num):
    total_fibonacci += a
    a, b = b, b + a
    
print("Sum of fibonacci series is", total_fibonacci)