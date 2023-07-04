class Student:      #always capital letters when doing classes
    def __init__(self, name, age, class_="student"): #
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, score1, score2, score3):
        average = (score1 + score2 + score3) /300 *100
        return f"{self.name} - average test: {average} %"

student1 = Student("john", 22, ) #
print(student1.average_test_score(20, 30, 40))

class Bird: #parent class
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly (self):
        print(f"{self.name} is with a wingspan of {self.wingspan}cm")


    def __str__(self): #will print out whatever you ask fom it
        return f"{self.name} ({self.__class__.__name__})"
    
class Owl(Bird): #child class to bird
    def __init__(self, name, wingspan, nocturnal=True):
        super().__init__(name, wingspan)
        self.nocturnal = nocturnal

    def hoot(self):
        print(f"{self.name} is hooting")   

    def __str__(self):
        return super().__str__() + f"- nocturnal:{self.nocturnal}"
    
class Dodo(Bird): #child class to bird
    def __init__(self, name, wingspan, extinct=True):
        super().__init__(name, wingspan)
        self.extinct = extinct

    def __str__(self):
        return super().__str__() + f" - extinct: {self.extinct}"
    

bird1 = Bird("eagle", 20)
owl1 = Owl("barn owl", 90)
dodo1 = Dodo("the dodo", 100)

bird1.fly()
print(bird1)

owl1.fly()
print(owl1)

dodo1.fly()
print(dodo1)