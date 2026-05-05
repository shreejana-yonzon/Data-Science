class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    

class User():
    def __init__(self, name, is_premium):
        self.user_name = name
        self.is_premium = is_premium
        
class ShoppingCart():
    def __init__(self, user):
        self.user = user
        self.items = []
        
    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} is added to {self.user.user_name}'s cart.")
        
    def remove_product(self,product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"{product_name} is removed form a cart.")
            else:
                print(f"{product_name} not found.")
        
    
    def calculate_total_cost(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
            
        
        if self.user.is_premium:
            discount = total_price * 0.10
            total_price -= discount 
            print(f"Premium member discount: Rs.{discount}")
        return total_price
    
    def invoice_generator(self):
        print(f"------------ Invoice for {self.user.user_name.upper()}------")
        
        if not self.items:
            print("Your cart is Empty.")
            return
        
        for item in self.items:
                print(f"-{item.name}: Rs {item.price}")
               
        
        final_total = self.calculate_total_cost()
        print(f"Total amount due: Rs{final_total}")
        
        

if __name__ == "__main__":
    
    #Create product
    print("-----------  List of Products  ----------------")
    p1 = Product("Iphone",250000)
    p2 = Product("Samsung",250000)
    p3 = Product("Oppo",250000)
    p4 = Product("Vivo",250000)


    #Create Premium user
    customer = User("Bob", is_premium=True)
    
    #shopping cart
    cart = ShoppingCart(customer)
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    cart.add_product(p4)

    #Remove an item
    cart.remove_product("Oppo")
    
    #Final Bill of all items
    cart.invoice_generator()