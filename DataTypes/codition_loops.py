# create dictionary from two given list
# a = ['name', 'age', 'grade']
# b = ['xyz', 10, 2]

# dict = {}

# for element in range(3):
#   dict[a[element]] = b[element]
# print(dict)


#check the existence of element in list
# input list with a search element
# output true or false

# num = [1,4,2,6,7,8,9,5]
# search_element = 8

# print(search_element in num)


#reverse list

#find the second largest number from the list
# list = [7,17,13,14,77,89]
# max_number = list[0]

# for element in list:
#     if element > max_number:
#         max_number = element
# print(max_number)
# second_lagNum = list[0]

#find sub list from list to match a sum value

# listing = [5,4,11,9,3]
# sum_value = 20

# current_sum = 0

# for element in range(listing):
#     current_sum += listing[element]
    
#     if current_sum == sum_value:
       
    

# output = [11,9]

# for element in listing:
   
# reposition all the zeros to end of the list

#example
# listing = [1,2,3,4,0,0,0,12]
# listing.sort(reverse=True)
# print(listing)

# output = [1,2,3,4,12,0,0,0]



#Break and continue in for loop

# a = [2,3,1,5,9,8]
# search_num = 1
# for element in a:
#     if element == search_num:
#         print('element found')
#         break
    
    
    
#continue
# voters_age = [18,19,20,21,22,23,24,25]

# for age in voters_age:
#     if age >= 18:
#         print("Voter id is being generated.")
#         continue # it skip and ignore code
#     print('not a voter')
#     print('Voter id is not being generated.')
#     remaining_age = 18 - age
#     print(f'{remaining_age}' + 'years remaining')

#while loop: until condition meets than it runs

# number = 10

# while number < 10:
#     print(number)
#     number += 1

stored_number = 55
max_attempts = 0

while max_attempts < 5:
    number1 = int(input('Enter the number between 1 to 100: '))
    
    if number1 == stored_number:
        print('number found')
        break
    elif number1 > stored_number:
        print('Entering number is too high.')
        
    else:
        print('Entering number is too low.')
        
    max_attempts+=1
        
    


