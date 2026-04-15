# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def eat(self):
#         print(f'{self.name} is eating')
    
#     def sleep(self):
#         print(f'{self.name} is sleeping')
    
    
# class Dog(Animal):
#     def __init__(self,name,color):
#         super().__init__(name)
#         self.color = color
        
#     def bark(self):
#         print(f'{self.name} is Barking.')
    
#     def eat(self):
#         print('Dog is eating')
#         return super().eat()
        
    


# dog1 = Dog('Sheru','white') #Creating object.
# print(dog1.color)
# print(dog1.eat()) # parent class has no return so it print none.
# dog1.eat()
# # dog1.sleep()
# # dog1.bark()
        
    
        
# class bird(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
    
#     def fly(self):
#         print(f'{self.name} is Barking.')
        
    
# bird1 = bird('albertrust', 'White')
# print(bird1.color)
# bird1.eat()
# bird1.sleep()
# bird1.fly()

#create a class for vehicle with attributes like name, model, year.
# methods like start_engine, stop_engine
# create a class for car which inherits from vehicle and has attributes like num_doors
# methods like open_doors,close_doors
# create a class for motorcycle which inherits from vehicle and has attributes like has_sidecar
# methods like open_sidecar, close_sidecar

# #Base Class
# class Vehicle:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year
    
#     def start_engine(self):
#         print(f'{self.name} engine started.')
    
    
#     def stop_engine(self):
#         print(f'{self.name} engine stopped')

# #Derived Class: car
# class Car(Vehicle):
#     def __init__(self, name, model, year, num_doors):
#         super().__init__(name, model, year)
#         self.num_doors = num_doors
    
#     def open_doors(self):
#         print(f'{self.name} has {self.num_doors} doors.Doors opened.')
        
#     def close_doors(self):
#         print(f'{self.name} has {self.num_doors} doors. Door closed.')

# #Derived Class: motorcycle
# class Motorcycle(Vehicle):
#     def __init__(self, name, model, year, has_sidecar):
#         super().__init__(name, model, year)
#         self.has_sidecar = has_sidecar
    
#     def open_sidecar(self):
#         if self.has_sidecar:
#             print(f'{self.name} sidecar opened.')
#         else:
#             print(f'{self.name} has no sidecar opened.')
        
#     def close_sidecar(self):
#         if self.has_sidecar:
#             print(f'{self.name} sidecar closed.')
#         else:
#             print(f'{self.name} has no sidecar.')
            
        

#---------------Usages-------------------------    
# vehicle1 = Vehicle('TVS', 'NTROQ', 2020)
# vehicle1.start_engine()
# vehicle1.stop_engine()   

# car1 = Car('Toyota','Corolla', 2022, 4)
# car1.close_doors()
# car1.open_doors()
# car1.start_engine()
# car1.start_engine()


# motorcycle1 = Motorcycle('Triumph', 'Scrambler 400X', 2020, True)
# motorcycle1.close_sidecar()
# motorcycle1.open_sidecar()
# motorcycle1.start_engine()
# motorcycle1.stop_engine()


#Multiple inheritance in OOPS:
# mro = method resolution order
# class GrandMother:
#     def __init__(self):
#         self.property5 = 'Land'
    
#     def height(self):
#         print('Height of grandmother')
        
# class GrandFather:
#     def __init__(self):
#         self.property6 = 'Gold'
    
#     def height(self):
#         print('Height of grandfather.')
        
# class Father:
#     def __init__(self):
#         self.property1 = 'House'
#         self.property2 = 'Car'
    
#     def height(self):
#         print('Height of father.')

# class Mother(GrandMother,GrandFather):
#     def __init__(self):
#         self.property3 = 'amenities'
#         self.property4 = 'Motorcycle'
#         super().__init__()
    

# class Child(Mother,Father):
#     def __init__(self):
#         self.property1 = 'House'
#         self.property2 = 'Car'
#         super().__init__()

# child1 = Child()
# print(child1.property3)
# print(child1.property4)
# print(child1.height())

# print(Child.__mro__)


#create a class for A,B,C,D,E
#A,B,C,D,E should inherit from each other in a way A,B,C,D,E
# and each class should have a __init__ method that prints the class name
# code to print class name is print(self.__class__.__name__)


# class E:
#     def __init__(self):
#         print(self.__class__.__name__)
# class D(E):
#     def __init__(self):
#         print(self.__class__.__name__)
#         super().__init__()
        
# class C(D):
#     def __init__(self):
#         print(self.__class__.__name__)
#         super().__init__()
        
# class B(C):
#     def __init__(self):
#         print(self.__class__.__name__)
#         super().__init__()
        
# class A(B):
#     def __init__(self):
#         print(self.__class__.__name__)
#         super().__init__()
# e = A()
# print(A.__mro__)

#polymorphism in oops: multiple behaviour in oops

# a = 10
# b = 10
# print(a+b)

# a = "10"
# b = "10"
# print(a+b)


# class Animal:
#     def speak(self):
#         print('Animal is speaking.')

# class Dog(Animal):
#     def speak(self):
#         print('Dog is speaking')
        
# class Cat(Animal):
#     def speak(self):
#         print('Cat is speaking')
        
# animal = Animal()
# dog = Dog()
# cat = Cat()
# animal.speak()
# dog.speak()
# cat.speak()


#classwork in polymorphism
#create a class for calculator with methods add,subtract,multiply,divide
#create a class for scientific calculator which inherits from calculator and
# has methods power,square_root,multiply with 10 to the power format
#create a class for programmer calculator which inherits from calculator and has methods
# binary_to_decimal,decimal_to_binary

#Base Class
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
        
#     def add(self):
#         sum = self.num1 + self.num2
#         print(f'The total sum of {self.num1} and {self.num2} is {sum}')
        
#     def subtract(self):
#         sub = self.num1 - self.num2
#         print(f'The difference of {self.num1} and {self.num2} is {sub}')
    
#     def multiply(self):
#         mul = self.num1 * self.num2
#         print(f'The multiplication of {self.num1} and {self.num2} is {mul}')
        
#     def divide(self):
#         division = self.num1 / self.num2
#         if self.num2 == 0:
#             print('It cannot be divided.')
#         else:
#             print(f'The division of {self.num1} and {self.num2} is {division}')


# #Derived class : ScientificCalculator
# class ScientificCalculator(Calculator):
    
#     def power(self):
        
#         power = self.num1 ** self.num2
#         print(f'The power of {self.num1} and {self.num2} is {power} ')
    
#     def square_root(self):
#         num = self.num1
#         i = 1
        
#         while i * i <= num:
#             if i * i == num:
#                 print(f'The square root of {num} is {i}')
#                 return
#             i += 1
#         print(f'Not a perfect square root')
            
        
            
        
#     def multiply_scientific(self):
#         mul = self.num1 * self.num2
#         power = 0
        
#         while mul >= 10:
#             mul /= 10
#             power += 1
            
#         print(f'The multiplication of {self.num1} and {self.num2} in Scientific form is : {mul} * 10^{power}')
        
     
# #------------Usages---------------
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# calc = ScientificCalculator(num1, num2) 

# calc.add()
# calc.subtract()
# calc.multiply()
# calc.divide()

# #For Scientific Calculator
# calc.power()
# calc.square_root()
# calc.multiply_scientific()


#classwork in polymorphism
#create a class for Vehicle with attributes model, year
#methods like start_engine, stop_engine
# create a class for Bike which inherits from vehicle and has attributes like num_wheels
# methods like open_sidecar, close_sidecar, start_engine, stop_engine
# create a class car which inherit from vehicle and has attributes like num_doors
#methods like open_doors,close_doors,start_engine,stop_engine

    
    
    
# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year 
    
#     def start_engine(self):
#         print(f'{self.model} engine started.')
    
#     def stop_engine(self):
#         print(f'{self.model} engine stopped.')


# class Bike(Vehicle):
#     def __init__(self, model, year, num_wheels):
#         super().__init__(model, year)   
#         self.num_wheels = num_wheels
    
#     def open_sidecar(self):
#         print(f'{self.model} sidecar opened.')
    
#     def close_sidecar(self):
#         print(f'{self.model} sidecar closed.')
    
#     # polymorphism (overriding)
#     def start_engine(self):
#         print(f'{self.model} bike engine roars to life!')

#     def stop_engine(self):
#         print(f'{self.model} bike engine turned off.')


# class Car(Vehicle):
#     def __init__(self, model, year, num_doors):
#         super().__init__(model, year)
#         self.num_doors = num_doors
    
#     def open_doors(self):
#         print(f'{self.model} doors opened.')
    
#     def close_doors(self):
#         print(f'{self.model} doors closed.')
    
#     # polymorphism (overriding)
#     def start_engine(self):
#         print(f'{self.model} car engine starts smoothly.')

#     def stop_engine(self):
#         print(f'{self.model} car engine stopped.')


# # Example usage
# v = Vehicle("Generic Vehicle", 2020)
# b = Bike("Yamaha", 2022, 2)
# c = Car("Toyota", 2023, 4)

# v.start_engine()
# b.start_engine()   
# c.start_engine()

# b.open_sidecar()
# c.open_doors()






# Python built in Polymorphism  max, + which add and concatenate , *: anything which deals with behavioural change called it polymorphism.
# print(max([1,3,4,5]))
# print(max(['ram', 'shyam','rohit']))
# print('A' *2)
# print([1]*2)

 
 
#create a class payment with attributes like amount, currency,
#and method pay
#create a class that inherits payment named as esewa 
#create a class that inherits payment named as khalti 
#create a class that inherits payment named as paypal
#each class should have a method pay and use polymorphism transfer method
#each class should have its own transfer_charge rate

# Base class
class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def pay(self):
        print("Payment in processing...")
    
    def transfer(self):
        print("Amount will be transfer...")
    


# Derived class: Esewa
class Esewa(Payment):
    
    def __init__(self, amount,currency, transfer_charge_rate):
        super().__init__(amount,currency)
        self.transfer_charge_rate = transfer_charge_rate
        
    def pay(self):
        print(f"Paying {self.amount} {self.currency} using Esewa.")
        
    def transfer(self):
        charge = self.amount * self.transfer_charge_rate
        total = self.amount + charge
        print(f"Transfer Charge of eSewa: {charge}, Total: {total}")


# Derived class: Khalti
class Khalti(Payment):
    def __init__(self, amount, currency, transfer_charge_rate):
        super().__init__(amount, currency)
        self.transfer_charge_rate = transfer_charge_rate
        
    def pay(self):
        print(f"Paying {self.amount} {self.currency} using Khalti.")
    
    def transfer(self):
        charge = self.amount * self.transfer_charge_rate
        total = self.amount + charge
        print(f"Transfer Charge of Khalti: {charge}, Total: {total}")


# Derived class: PayPal
class Paypal(Payment):
    def __init__(self, amount, currency,transfer_charge_rate):
        super().__init__(amount, currency)
        self.transfer_charge_rate = transfer_charge_rate
        
    def pay(self):
        print(f"Paying {self.amount} {self.currency} using PayPal.")

    def transfer(self):
        charge = self.amount * self.transfer_charge_rate
        total = self.amount + charge
        print(f"Transfer Charge of paypal: {charge}, Total: {total}")
        
# --------------------usage--------------------
e = Esewa(1000, "NPR", 10)
k = Khalti(500, "NPR", 0.3)
p = Paypal(20, "USD",15)

e.pay()
e.transfer()
k.pay()
p.pay()
