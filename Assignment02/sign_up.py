class UnderageError(Exception):
    """Custom error for when a user didn't meet targeted age."""
    pass

def register_user(): 
    try:
        user_name = input("Enter your name: ")
        age = int(input(f"Hello! {user_name}. \nEnter your age: "))
        
        if age < 18:
             raise UnderageError(f"Oops! {user_name}, you are under age. Must be 18+ to view this movie.")
        
        print(f"Welcome to MovieTime, {user_name}. Enjoy your Movie.")
        
    except ValueError:
        print("Invalid input! Age must be in number.")
    
    except UnderageError as err:
        print(f"Access restricted. {err}")
    
    finally:
        print("Thank you for using MovieTime")
        
    
    
if __name__ == "__main__":
    register_user()