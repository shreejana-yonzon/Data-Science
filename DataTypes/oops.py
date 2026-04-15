
class BankAccount:
    def __init__(self, account_number,account_holder_name,balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.bank_name = 'Nepal Bank'
        self.__balance = balance #private/protected __ balance
        
    def check_balance(self):
        return self.__balance
    
    def deposit_balance(self, amount):
        """Deposits an amount into the account."""
        if amount > 0:
            self.__balance += amount
        else:
            "Deposit amount must be positive."
            
        return self.__balance
    
    def withdraw_balance(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            "Insufficient balance"
        return self.__balance
      


bank_account1 = BankAccount(123456,'John Doe', 1000)
bank_account2 = BankAccount(798023,' Steven Roe', 10000)

# print(bank_account1.check_balance())
print(BankAccount.check_balance(bank_account1))

print(BankAccount.deposit_balance(bank_account1,100))

print(BankAccount.withdraw_balance(bank_account1,1000))

print(BankAccount.check_balance(bank_account1))



# print(bank_account1.account_number)
# print(bank_account1.account_holder_name)
# print(bank_account1.bank_name)

# Create a class for student with attributes like name, age, grade, subject, score
#methods like get_score to access private score attribute
# and set_score to set private sore attribute


class Student:
    def __init__(self, name, age, grade, subject, score):
        self.name = name
        self.age = age
        self.grade = grade
        self.subject = subject
        self.__score = score
    
    # Getter method
    def get_score(self):
        """student's score."""
        return self.__score

    # Setter method
    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
            return self.__score
        else:
            "Score must be between 0 and 100."

student1 = Student("Ram", 20, "A", "Math", 80)
print(student1.get_score())
print(student1.set_score(90))
print(student1.get_score()) 

#create a class name cart 
#attributes like items which should be private attributes
#methods like add_item to add item to cart, remove item from cart and 
#display_items to display all items in cart

class Cart:
    def __init__(self):
        self.__items = []
    
    def add_item(self,item):
        self.__items.append(item)
        print(f"'{item}' has been added to the cart.")
    
    def remove_item(self, item):
    
        if item in self.__items:
            self.__items.remove(item)
            print(f"'{item}' has been removed from the cart.")
        else:
            print(f"'{item}' was not found in the cart.")
    
    def display_items(self):
        for item in self.__items:
            print(item)
        


cart = Cart()

# Add items
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Grapes")
cart.display_items() 

# Remove items
cart.remove_item("Banana")

# Display items
cart.display_items() 



#create a class for LeaveBalance
#attributes like leave_balance which should be private attribute
#leave balance should be a list of dict
#dict should contain name, leave_type, total_leaves
#private method to (add_leave,deduct_leave,get_leave_balance)
#and public method to get leave balance and set leave balance .

class LeaveBalance:
    def __init__(self):
        self.__leave_balance = [
            {
                'name' : 'Ram',
                'leave_type': 'Sick',
                'total_leave':5
            }
            ] #private attribute: list of dict
    
    def __add_leave(self, dictionary_value):
        for leave in self.__add_leave:
            if leave.get('name') == dictionary_value.get('name') and leave.get('leave_type') == dictionary_value.get('leave_type'):
                leave['total_leave'] += dictionary_value['total_leave']
                
            else:
                 self.__leave_balance.append(dictionary_value)
                 

    def __deduct_leave(self, name, deduct_value):
        for leave in self.__deduct_leave:
            if leave.get('name') == deduct_value.get('name') and leave.get('total_leave') == deduct_value.get('total_leave'):
                leave['total_leave'] -= deduct_value ['total_leave']
            else:
                """value cannot be deducted!!"""
    
    
    
    # Getter and Setter methods
    
    def get_leave_balance(self, name):
       record = self.get_leave_balance(name)
       
            
            









#---------------Usage------------
lb = LeaveBalance()
# Add leave Records




# class LeaveBalance:
#     def __init__(self):
#         self.__leave_balance = []  # Private attribute: list of dicts

#     # ── Private Methods ────────────────────────────────────────────────

#     def __add_leave(self, name, leave_type, total_leaves):
#         """Private: Adds a new leave record to the balance list."""
#         for record in self.__leave_balance:
#             if record["name"] == name and record["leave_type"] == leave_type:
#                 print(f"Leave record for '{name}' ({leave_type}) already exists.")
#                 return

#         self.__leave_balance.append({
#             "name"             : name,
#             "leave_type"       : leave_type,
#             "total_leaves"     : total_leaves,
#             "remaining_leaves" : total_leaves
#         })
#         print(f"Leave record added for '{name}' ({leave_type}).")

#     def __deduct_leave(self, name, leave_type, days):
#         """Private: Deducts leave days from a matching record."""
#         for record in self.__leave_balance:
#             if record["name"] == name and record["leave_type"] == leave_type:
#                 if days <= 0:
#                     print("Deduction days must be greater than 0.")
#                     return
#                 if record["remaining_leaves"] >= days:
#                     record["remaining_leaves"] -= days
#                     print(f"{days} day(s) deducted for '{name}' ({leave_type}). "
#                           f"Remaining: {record['remaining_leaves']}")
#                 else:
#                     print(f"Insufficient leave balance for '{name}' ({leave_type}). "
#                           f"Available: {record['remaining_leaves']} day(s).")
#                 return
#         print(f"No record found for '{name}' ({leave_type}).")

#     def __get_leave_balance(self, name):
#         """Private: Retrieves all leave records for a given employee."""
#         records = [r for r in self.__leave_balance if r["name"] == name]
#         return records if records else None

#     # ── Public Methods ─────────────────────────────────────────────────

#     def get_leave_balance(self, name):
#         """Public: Displays leave balance for a given employee."""
#         records = self.__get_leave_balance(name)
#         if records:
#             print(f"\nLeave Balance for '{name}':")
#             print(f"  {'Leave Type':<20} {'Total':>6} {'Remaining':>10}")
#             print(f"  {'-'*38}")
#             for r in records:
#                 print(f"  {r['leave_type']:<20} {r['total_leaves']:>6} {r['remaining_leaves']:>10}")
#         else:
#             print(f"No leave records found for '{name}'.")

#     def set_leave_balance(self, action, name, leave_type, value):
#         """
#         Public: Interface to modify leave balance.
#         Actions: 'add'    -> add_leave(name, leave_type, total_leaves)
#                  'deduct' -> deduct_leave(name, leave_type, days)
#         """
#         if action == "add":
#             self.__add_leave(name, leave_type, value)
#         elif action == "deduct":
#             self.__deduct_leave(name, leave_type, value)
#         else:
#             print(f"Unknown action '{action}'. Use 'add' or 'deduct'.")


# # ── Usage ──────────────────────────────────────────────────────────────

# lb = LeaveBalance()

# # Add leave records
# lb.set_leave_balance("add", "Alice", "Sick Leave",   15)
# lb.set_leave_balance("add", "Alice", "Casual Leave", 10)
# lb.set_leave_balance("add", "Bob",   "Sick Leave",   15)

# # Display leave balance
# lb.get_leave_balance("Alice")
# lb.get_leave_balance("Bob")

# # Deduct leaves
# lb.set_leave_balance("deduct", "Alice", "Sick Leave",   3)
# lb.set_leave_balance("deduct", "Alice", "Casual Leave", 7)
# lb.set_leave_balance("deduct", "Bob",   "Sick Leave",  20)  # Insufficient

# # Display updated balance
# lb.get_leave_balance("Alice")

# # Duplicate entry check
# lb.set_leave_balance("add", "Alice", "Sick Leave", 15)

# # Invalid action
# lb.set_leave_balance("update", "Alice", "Sick Leave", 5)
        
        
        
        
        
        
        
        
        
        
        
# class LeaveBalance:
#     def __init__(self):
#         self.__leave_balance = [{
#             'name' : 'Supriya',
#             'leave_type' : 'Sick',
#             'total_leave':12
#         }]

#     def __add_leave(self,dict_value):
#         print(dict_value)
#         print(self.__leave_balance)
    
#         for leave in self.__leave_balance:
#             if leave.get('name') == dict_value.get('name'):
#                 leave['total_leave'] += dict_value['total_leave']
#             else:
#                 self.__leave_balance.append(dict_value)
#                 break 


#     def __deduct_leave(self,name,deduct_value):
#         for leave in self.__leave_balance:
#             if leave.get('name') == name and leave.get('total_leave') >= deduct_value:
#                  leave['total_leave'] -= deduct_value
#                  return True
            
#         return False


        

#     def get_leave_balance(self,name):
#         print(self.__leave_balance)
#         for leave in self.__leave_balance:
#             if leave.get('name') == name:
#                 return leave.get('total_leave')
            

    
#     def set_leave_balance(self,action,dict_value=None,name=None,deduct_value=None):
#         if action == "add":
#             self.__add_leave(dict_value)
#         elif action == 'deduct':
#             print('working')
#             self.__deduct_leave(name,deduct_value)
#         else:
#             return 'invalid action'
        

# leave_object = LeaveBalance()

# leave_object.set_leave_balance(
#     'add',
#     {
#         'name':'Yugan',
#         'leave_type':'Casual',
#         'total_leave':10
#     }
# )


# leave_object.set_leave_balance(
#     'deduct',name='Yugan',deduct_value=5)

# print(leave_object.get_leave_balance('Yugan'))