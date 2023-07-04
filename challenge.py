#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length * self.width)
    
rect = Rectangle(45, 90)
print(rect.area())
print(rect.perimeter())

class Car:      #always capital letters when doing classes
    def __init__(self, make, model, year): #
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make
    
    def set_make(self, make):
        self.make = make
    
    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    
car = Car("BMW", "X5", 2020)
print(car.get_make())  
print(car.get_model())  
print(car.get_year())   
print(car)  
    