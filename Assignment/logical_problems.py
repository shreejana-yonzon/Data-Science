#prime numbers checker
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break                                 #break is use to stop the condition after meet the condition
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    
#reverse a number
num = input("Enter a number:")
#Using slicing methods 
reverse_num = num[::-1]                         
print("Reverse number: ", reverse_num)


#count digits in a number
#Method using the len function
num = input("Enter numbers: ")
print("Number of digits = ", len(num))


#Number guessing game(basic)
#(Optional) Armstrong number checker