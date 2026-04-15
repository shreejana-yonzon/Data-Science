class Number:
    def __init__(self, num):
        self.num = num
    
#----Special method-----
    def __add__(self,other):  
        return self.num - other.num
    
    def __str__(self):
        
        print('Check if it is being called or not!')
        return str(self.num)





num1 = Number(10)
num2 = Number(20)
print(type(num1))
print(type(num2))
print(type(num1 + num2))


result = num1 + num2
print(result)
print(num2)


# print(obj1 + obj2)
# print(obj1.__add__(obj2))


#create a class for vector with attributes x,y
#methods add
#methods should use operator overloading

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self):
        return self.x + self.y
    
    
        