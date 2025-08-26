#Write a class calculator capable of finding square, cube and squareroot of a rumber!
import math

class Calculator:
    def __init__(self, number):
        self.number = number
    
    def square(self):
        print(f"The square of {self.number} is {self.number ** 2}")
    
    def cube(self):
        print(f"The cube of {self.number} is {self.number ** 3}") 
    
    def squareroot(self):
        print(f"The square root of {self.number} is {math.sqrt(self.number)}")

number = int(input("Enter a number: "))
cal = Calculator(number)
cal.square()
cal.cube()
cal.squareroot()

